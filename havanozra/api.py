import frappe
from frappe import _, msgprint, throw
import json
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
            max_net_rate = 0.0
            
            if tax_info and len(tax_info) > 0:
                tax_category = tax_info[0].tax_category
                max_net_rate = float(tax_info[0].maximum_net_rate or 0)
                max_net_rate = max_net_rate / 100

            if tax_category is None:
                msgprint("Tax Information is missing for one or more Item, Please update Item Tax Information")
                return  "Cannot send invoice to zimra"
            
            # Calculate VAT (tax is inclusive in price)
            tax_rate = max_net_rate / 100
            vat_amt = item.amount * tax_rate / (1 + tax_rate)
        
            item_total = round(item.amount,2)
            vat_amt = round(vat_amt,2)
            
            
            # If tax exclusive, logic changes, but following VB 'Inclusive' assumption:
            supply_amount = item.amount - vat_amt
            supply_amount = round(supply_amount,2)
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
                <SplyAmt>{supply_amount or 0}</SplyAmt>
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
            </ITEM>
            """
            xml_string += item_xml

        xml_string += "</ITEMS>"

        # 5. Call ZRA Send Invoice
        frappe.log_error(f"Havano ZRA Log", f"Attempting to Send Invoice {cis_invoice_no}")
        
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
            exchange_rate="1", # Assuming default 1 if not provided, or pull from doc
            destn_country_code=None,
            items_xml=xml_string
        )

        # 6. Parse Response
        response_data = json.loads(response_json)
        result_msg = response_data.get("resultMsg")
        result_cd = response_data.get("resultCd")
        
        if result_msg == "It is succeeded" or result_cd == "000":
            frappe.log_error(f"Havano ZRA Log", f"Successfully Sent Invoice {cis_invoice_no}")
            
            # Extracting details from ZRA response (based on VB guide)
            # Note: Ensure your Python library's SendInvoice parses these fields correctly
            if response_data.get("data"):
                zra_rcpt_no = response_data["data"].get("rcptNo")
                zra_qr_code = response_data["data"].get("qrCodeUrl")
                
                # Update Frappe Doc with ZRA details
                # doc.db_set("custom_zra_receipt_no", zra_rcpt_no)
                # doc.db_set("custom_zra_qr_code", zra_qr_code)
                
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
        frappe.log_error(f"Invalid JSON response from ZRA: {response_json}", "ZRA Send Invoice Failed")
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