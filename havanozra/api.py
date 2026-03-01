import frappe
from frappe import _, msgprint, throw
import json
import qrcode
import base64
from io import BytesIO
from havanozra.zra_action import HavanoZRALib


def extract_value(text: str) -> str:
    return text.split(" - ", 1)[0].strip()

@frappe.whitelist()
def push_item(doc, method):
    print("Preparing to send item to ZRA.....")
    item_vat_code = frappe.get_value(
            "Item Tax",{"parent": doc.item_code},"tax_category")
    item_price = frappe.db.get_value("Item Price",{"item_code": doc.item_code,"price_list": "Standard Selling"},"price_list_rate")
    item_selling_price =0
    selling_price = doc.standard_rate
    if item_price:
        item_selling_price = item_price 
    else:
        item_selling_price = selling_price
    
    if (item_vat_code==None):
        msgprint("Item Vat Information is missing, please update vat information")
        return  ""
    item_cc = extract_value(doc.custom_item_classification_code)
    item_pt = extract_value(doc.custom_item_product_type)
    item_coo = extract_value(doc.custom_item_country_of_origin)
    item_puc = extract_value(doc.custom_packaging_unit_code)
    item_ipl_cc= extract_value(doc.custom_ipl_category_code)
    item_tl_cc = extract_value(doc.custom_tl_category_code)
    if item_ipl_cc == "N/A":
        item_ipl_cc = None
    
    if item_tl_cc == "N/A":
        item_tl_cc = None
    #print(item_vat_code)
        
    zra_lib = HavanoZRALib()
    
    creator_username = "Admin"
    creator_user_id = "Admin"
    modifier_username = "Admin"
    modifier_user_id = "Admin"

    try:
        frappe.log_error(f"Havano ZRA Log",f"Attempting to save Item {doc.item_code}")
        response_json = zra_lib.save_item(doc.item_code, item_cc, 
                                          item_pt,doc.item_name,
                                          doc.item_name,item_coo,
                                          item_puc,doc.stock_uom,  
                                          item_vat_code,item_ipl_cc,
                                          item_tl_cc,None,None,None, 
                                          item_selling_price, None,"1","N","Y",
                                          creator_username,
                                          creator_user_id,
                                          modifier_username,
                                          modifier_user_id)

        # 4. Parse the response to check success
        response_data = json.loads(response_json)
        result_msg = response_data.get("resultMsg")
        result_cd = response_data.get("resultCd")
        
        if result_msg == "It is succeeded" or result_cd == "000":
            frappe.log_error(f"Havano ZRA Log",f"Successfully saved Item {doc.item_code}")
            return {
                "status": "success",
                "message": "Item synced successfully with ZRA.",
                "data": response_data
            }
        else:
            error_msg = f"ZRA Error for {doc.item_code}: {result_msg}"
            frappe.log_error(f"Havano ZRA Error",error_msg)
            return {
                "status": "error",
                "message": error_msg,
                "data": response_data
            }

    except json.JSONDecodeError:
        frappe.log_error(f"Invalid JSON response from ZRA: {response_json}", "ZRA Save Item Failed")
        return {
            "status": "error",
            "message": "Invalid response received from ZRA server.",
            "response_raw": response_json
        }
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "ZRA Save Item Failed")
        return {
            "status": "error",
            "message": str(e)
        }
def push_item_update(doc, method):
    print("Preparing to UPDATE item to ZRA.....")
    item_vat_code = frappe.get_value(
            "Item Tax",{"parent": doc.item_code},"tax_category")
    item_price = frappe.db.get_value("Item Price",{"item_code": doc.item_code,"price_list": "Standard Selling"},"price_list_rate")
    item_selling_price =0
    selling_price = doc.standard_rate
    if item_price:
        item_selling_price = item_price 
    else:
        item_selling_price = selling_price
    
    #print(item_selling_price)  
    if (item_vat_code==None):
        frappe.msgprint("Item Vat Information is missing, please update vat information")
        return  ""
    
    # Assuming extract_value is a helper function in your environment
    item_cc = extract_value(doc.custom_item_classification_code)
    item_pt = extract_value(doc.custom_item_product_type)
    item_coo = extract_value(doc.custom_item_country_of_origin)
    item_puc = extract_value(doc.custom_packaging_unit_code)
    item_ipl_cc= extract_value(doc.custom_ipl_category_code)
    item_tl_cc = extract_value(doc.custom_tl_category_code)
    
    if item_ipl_cc == "N/A":
        item_ipl_cc = None
    
    if item_tl_cc == "N/A":
        item_tl_cc = None
    #print(item_vat_code)
        
    zra_lib = HavanoZRALib()
    
    creator_username = "Admin"
    creator_user_id = "Admin"
    modifier_username = "Admin"
    modifier_user_id = "Admin"

    try:
        frappe.log_error(f"Havano ZRA Log",f"Attempting to UPDATE Item {doc.item_code}")
        
        # Calling zra_lib.update_item instead of save_item
        response_json = zra_lib.update_item(doc.item_code, item_cc, 
                                          item_pt,doc.item_name,
                                          doc.item_name,item_coo,
                                          item_puc,doc.stock_uom,  
                                          item_vat_code,item_ipl_cc,
                                          item_tl_cc,None,None,None, 
                                          doc.standard_rate, None,"1","N","Y",
                                          creator_username,
                                          creator_user_id,
                                          modifier_username,
                                          modifier_user_id)

        # 4. Parse the response to check success
        response_data = json.loads(response_json)
        result_msg = response_data.get("resultMsg")
        result_cd = response_data.get("resultCd")
        
        if result_msg == "It is succeeded" or result_cd == "000":
            frappe.log_error(f"Havano ZRA Log",f"Successfully UPDATED Item {doc.item_code}")
            return {
                "status": "success",
                "message": "Item updated successfully with ZRA.",
                "data": response_data
            }
        else:
            error_msg = f"ZRA Error for {doc.item_code}: {result_msg}"
            frappe.log_error(f"Havano ZRA Error",error_msg)
            return {
                "status": "error",
                "message": error_msg,
                "data": response_data
            }

    except json.JSONDecodeError:
        frappe.log_error(f"Invalid JSON response from ZRA: {response_json}", "ZRA Update Item Failed")
        return {
            "status": "error",
            "message": "Invalid response received from ZRA server.",
            "response_raw": response_json
        }
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "ZRA Update Item Failed")
        return {
            "status": "error",
            "message": str(e)
        }
def get_exchange_rate(from_currency: str, to_currency: str):
    if from_currency == to_currency:
        return 1
    exchange_rate = frappe.db.get_value(
        "Currency Exchange",
        {
            "from_currency": from_currency,
            "to_currency": to_currency
        },
        "exchange_rate"
    )

    if not exchange_rate:
        frappe.throw(f"No exchange rate found for {from_currency} to {to_currency}")
    return exchange_rate

def get_current_item_qty(item_code: str):
    qty = frappe.db.get_value(
        "Bin",
        {
            "item_code": item_code
        },
        "actual_qty"
    )
    return qty or 0

def push_invoice_to_zra(doc, method):
    print("Preparing to send Invoice to ZRA.....")
    
    zra_lib = HavanoZRALib()
    
    creator_username = "Admin"
    creator_user_id = "Admin"
    modifier_username = "Admin"
    modifier_user_id = "Admin"

    # 3. Extract Invoice Level Data
    cis_invoice_no = doc.name
    customer_name = doc.customer_name
    currency_code = doc.currency
    iscreditnote = doc.is_return
    invoice_receiptno = ""
    if iscreditnote:
        print (f"Credit note: {iscreditnote}")
        invoice_cr = frappe.get_all("Sales Invoice",
    filters={"name": cis_invoice_no},fields=["custom_receiptno"]
    )
        for inv in invoice_cr:
            invoice_receiptno = inv.custom_receiptno
    customer_tpin = frappe.db.get_value("Customer", doc.customer, "custom_customer_tpin")
    
    xml_string = "<ITEMS>"
    total_item_count = 0
    items = frappe.get_all(
    "Sales Invoice Item",
    filters={"parent": cis_invoice_no},
    fields=["item_code", "item_name", "qty", "rate", "amount"]
    )
    try:
        for item in items:
            total_item_count += 1
            # item_info = frappe.get_all(
            # "Item",filters={"item_code": item.item_code},
            # fields=["item_code","custom_item_classification_code","custom_item_product_type","custom_item_country_of_origin","custom_packaging_unit_code"])
            item_info = frappe.get_doc("Item", item.item_code)
            
            item_cc = extract_value(item_info.custom_item_classification_code)
            item_pt = extract_value(item_info.custom_item_product_type) # Not used in XML below but kept for logic
            item_coo = extract_value(item_info.custom_item_country_of_origin)
            item_puc = extract_value(item_info.custom_packaging_unit_code)
            itemvatcode = frappe.get_all(
            "Item Tax",
            filters={"parent": item_info.item_code},
            fields=["tax_category"]
        )
            item_vat_code = itemvatcode[0].tax_category

            item_vat_cc = item_vat_code
            item_ipl_cc = extract_value(item_info.custom_ipl_category_code)
            item_tl_cc = extract_value(item_info.custom_tl_category_code)
            item_excise_cc = "N/A"

            if item_ipl_cc == "N/A": item_ipl_cc = None
            if item_tl_cc == "N/A": item_tl_cc = None
            if item_excise_cc == "N/A": item_excise_cc = None
            
            tax_info = frappe.get_all(
            "Item Tax",
            filters={"parent": item.item_code},
            fields=["tax_category", "maximum_net_rate"])
            
            tax_category = None
            tax_rate = 0.0
            
            if tax_info and len(tax_info) > 0:
                tax_category = tax_info[0].tax_category
                tax_rate = float(tax_info[0].maximum_net_rate or 0)
                tax_rate = tax_rate / 100

            if tax_category is None:
                msgprint("Tax Information is missing for one or more Item, Please update Item Tax Information")
                return  "Cannot send invoice to zimra"
            
            # Calculate VAT (tax is inclusive in price)

            vat_amt = abs(item.amount) * tax_rate / (1 + tax_rate)
            print(item.amount)
            item_total = abs(round(item.amount,4))
            vat_amt = round(vat_amt,4)
            print(vat_amt)
            
            
            # If tax exclusive, logic changes, but following VB 'Inclusive' assumption:
            supply_amount = abs(item.amount) - vat_amt
            supply_amount = round(supply_amount,4)
            # Defaults for non-VAT taxes (as per VB guide)
            excise_taxbl_amt = "0.0"
            tl_taxbl_amt = "0.0"
            ipl_taxbl_amt = "0.0"
            ipl_amt = "0.0"
            tl_amt = "0.0"
            excise_tx_amt = "0.0"
            
            # Discount
            discount_rate = item.discount_percentage if item.discount_percentage else 0
            discount_amt = item.discount_amount if item.discount_amount else 0
            
            # XML Construction (String formatting equivalent to VB String.Format)
            item_xml = f"""
            <ITEM>
                <ItemSeq>{total_item_count}</ItemSeq>
                <ItemCd>{item.item_code or ''}</ItemCd>
                <ItemClsCd>{item_cc or ''}</ItemClsCd>
                <ItemNm>{item.item_name or ''}</ItemNm>
                <Bcd>{item.barcode or ''}</Bcd>
                <PkgUnitCd>{item_puc or ''}</PkgUnitCd>
                <Pkg>0</Pkg>
                <QtyUnitCd>{item_puc}</QtyUnitCd>
                <Qty>{item.qty or 0}</Qty>
                <Prc>{item.rate or 0}</Prc>
                <SplyAmt>{item.amount }</SplyAmt>
                <DcRt>{discount_rate}</DcRt>
                <DcAmt>{discount_amt}</DcAmt>
                <IsrccCd></IsrccCd>
                <IsrccNm></IsrccNm>
                <IsrcRt>0</IsrcRt>
                <IsrcAmt>0</IsrcAmt>
                <VatCatCd>{item_vat_cc or ''}</VatCatCd>
                <ExciseTxCatCd>{item_excise_cc or ''}</ExciseTxCatCd>
                <TlCatCd>{item_tl_cc or ''}</TlCatCd>
                <IplCatCd>{item_ipl_cc or ''}</IplCatCd>
                <VatTaxblAmt>{supply_amount or 0}</VatTaxblAmt>
                <VatAmt>{vat_amt}</VatAmt>
                <ExciseTaxblAmt>{excise_taxbl_amt}</ExciseTaxblAmt>
                <TlTaxblAmt>{tl_taxbl_amt}</TlTaxblAmt>
                <IplTaxblAmt>{ipl_taxbl_amt}</IplTaxblAmt>
                <IplAmt>{ipl_amt}</IplAmt>
                <TlAmt>{tl_amt}</TlAmt>
                <ExciseTxAmt>{excise_tx_amt}</ExciseTxAmt>
                <TotAmt>{item_total or 0}</TotAmt>
                 <Rqty>{get_current_item_qty(item.item_code)}</Rqty>
            </ITEM>
            """
            xml_string += item_xml

        xml_string += "</ITEMS>"

        # 5. Call ZRA Send Invoice
        frappe.log_error(f"Havano ZRA Log", f"Attempting to Send Invoice {cis_invoice_no}")
        ex_rate = get_exchange_rate(currency_code, "ZMW")
        response_json = ""
        if iscreditnote:
            response_json = zra_lib.send_credit_note(invoice_receiptno,
            cis_invoice_no=cis_invoice_no,
            customer_tpin=customer_tpin,
            customer_name=customer_name,
            total_item_count=total_item_count,
            remark=None,
            creator_username=creator_username,
            creator_user_id=creator_user_id,
            modifier_username=modifier_username,
            modifier_user_id=modifier_user_id,
            lpo_number=None,
            currency_code=currency_code,
            exchange_rate=ex_rate, # Assuming default 1 if not provided, or pull from doc
            destn_country_code=None,
            ref_reason = "Customer Return",
            items_xml=xml_string
            )
        else:
            response_json = zra_lib.send_invoice(
            cis_invoice_no=cis_invoice_no,
            customer_tpin=customer_tpin,
            customer_name=customer_name,
            total_item_count=total_item_count,
            remark=None,
            creator_username=creator_username,
            creator_user_id=creator_user_id,
            modifier_username=modifier_username,
            modifier_user_id=modifier_user_id,
            lpo_number=None,
            currency_code=currency_code,
            exchange_rate=ex_rate, # Assuming default 1 if not provided, or pull from doc
            destn_country_code=None,
            items_xml=xml_string
            )

        # Parse Response
        response_data = json.loads(response_json)
        result_msg = response_data.get("resultMsg")
        result_cd = response_data.get("resultCd")
        
        if result_msg == "It is succeeded" or result_cd == "000":
            frappe.log_error(f"Havano ZRA Invoice Sent for {cis_invoice_no}", f"Response: {response_data}")
            
            if response_data.get("data"):
                zra_rcpt_no = response_data["data"].get("rcptNo")
                zra_qr_code = response_data["data"].get("qrCodeUrl")
                update_sales_invoice(cis_invoice_no,zra_rcpt_no,zra_qr_code)
            #Save Stock Section
            save_stock_response_json = zra_lib.save_stock_item(
            cis_invoice_no=cis_invoice_no,
            customer_tpin=customer_tpin,
            customer_name=customer_name,
            total_item_count=total_item_count,
            remark=None,
            creator_username=creator_username,
            creator_user_id=creator_user_id,
            modifier_username=modifier_username,
            modifier_user_id=modifier_user_id,
            items_xml=xml_string
            )
            
            response_data_save_stock = json.loads(save_stock_response_json)
            result_msg_save_stock = response_data.get("resultMsg")
  
            #if result_msg_save_stock == "It is succeeded":
            #SaveStockMaster Section
            stock_master_response_json = zra_lib.save_stock_master(
            creator_username=creator_username,
            creator_user_id=creator_user_id,
            items_xml=xml_string
            )
            
            response_data_save_stock = json.loads(stock_master_response_json)
            result_msg_stock_master = response_data.get("resultMsg")
            
            
                
               
                
            return {
                "status": "success",
                "message": "Invoice synced successfully with ZRA.",
                "data": response_data
            }
        else:
            error_msg = f"ZRA Error for Invoice {cis_invoice_no}: {result_msg}"
            frappe.log_error(f"Havano ZRA Error", error_msg)
            return {
                "status": "error",
                "message": error_msg,
                "data": response_data
            }

    except json.JSONDecodeError:
        frappe.log_error(f"Invalid JSON response from ZRA", f"ZRA Send Invoice Failed: {{response_json}}")
        return {
            "status": "error",
            "message": "Invalid response received from ZRA server.",
            "response_raw": response_json
        }
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "ZRA Send Invoice Failed")
        return {
            "status": "error",
            "message": str(e)
        }

def generate_qr_base64(data: str) -> str:
    """Generate a base64-encoded PNG image from the given data string."""
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return f"data:image/png;base64,{img_base64}"

def update_sales_invoice(invoice_name: str, receipt_no: str,  qr_code_data: str):
    try:
        sales_invoice = frappe.get_doc("Sales Invoice", invoice_name)
        qr_base64 = generate_qr_base64(qr_code_data)
        
        #Update custom fields
        if receipt_no is None:
            zra_status = None
        else:
            zra_status=1
        sales_invoice.custom_zra_status = zra_status
        sales_invoice.custom_receiptno = receipt_no
        sales_invoice.custom_qr_code = qr_base64  # You can also store just the base64 string
        
        # Save and commit
        sales_invoice.save(ignore_permissions=True)
        frappe.db.commit()
        return True
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Failed to update Sales Invoice")
        frappe.msgprint(f"Error: {e}")
        return False