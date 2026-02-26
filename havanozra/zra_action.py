import json
import os
import requests
from decimal import Decimal
from typing import List, Optional, Dict, Any
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

# Frappe Import
import frappe

# ==========================================
# Data Models
# ==========================================

@dataclass
class InvoiceItem:
    ItemSeq: int
    ItemCd: str
    ItemClsCd: str
    ItemNm: str
    Bcd: str
    PkgUnitCd: str
    Pkg: int
    QtyUnitCd: str
    Qty: int
    Prc: Decimal
    SplyAmt: Decimal
    DcRt: Decimal
    DcAmt: Decimal
    IsrccCd: str
    IsrccNm: str
    IsrcRt: Decimal
    IsrcAmt: Decimal
    VatCatCd: str
    ExciseTxCatCd: str
    TlCatCode: str
    IplCatCd: str
    VatTaxblAmt: Decimal
    VatAmt: Decimal
    ExciseTaxblAmt: Decimal
    TlTaxblAmt: Decimal
    IplTaxblAmt: Decimal
    IplAmt: Decimal
    TlAmt: Decimal
    ExciseTxAmt: Decimal
    TotAmt: Decimal

@dataclass
class ItemCls:
    itemClsCd: str
    itemClsNm: str
    itemClsLvl: int
    taxTyCd: str
    mjrTgYn: str
    useYn: str

@dataclass
class Data:
    itemClsList: List[ItemCls] = field(default_factory=list)

@dataclass
class RootObject:
    resultCd: str
    resultMsg: str
    resultDt: str
    data: Data

@dataclass
class SaveStockItems_ItemList:
    itemSeq: int
    itemCd: str
    itemClsCd: str
    itemNm: str
    bcd: str
    pkgUnitCd: str
    pkg: int
    qtyUnitCd: str
    qty: Decimal
    prc: Decimal
    splyAmt: Decimal
    totDcAmt: Decimal
    taxblAmt: Decimal
    vatCatCd: str
    taxAmt: Decimal
    totAmt: Decimal

@dataclass
class SaveStockItems:
    tpin: str
    bhfId: str
    sarNo: int
    orgSarNo: int
    regTyCd: str
    custTpin: str
    custNm: str
    custBhfId: str
    sarTyCd: str
    ocrnDt: str
    totItemCnt: int
    totTaxblAmt: Decimal
    totTaxAmt: Decimal
    totAmt: Decimal
    remark: str
    regrId: str
    regrNm: str
    modrNm: str
    modrId: str
    itemList: List[SaveStockItems_ItemList] = field(default_factory=list)

@dataclass
class SavePurchase_ItemList:
    itemSeq: int
    itemCd: str
    itemClsCd: str
    itemNm: str
    bcd: str
    pkgUnitCd: str
    pkg: int
    qtyUnitCd: str
    qty: Decimal
    prc: Decimal
    splyAmt: Decimal
    dcRt: Decimal
    dcAmt: Decimal
    taxTyCd: str
    iplCatCd: str
    tlCatCd: str
    exciseCatCd: str
    taxblAmt: Decimal
    vatCatCd: str
    iplTaxblAmt: Decimal
    tlTaxblAmt: Decimal
    exciseTaxblAmt: Decimal
    taxAmt: Decimal
    iplAmt: Decimal
    tlAmt: Decimal
    exciseTxAmt: Decimal
    totAmt: Decimal

@dataclass
class SavePurchase:
    tpin: str
    bhfId: str
    invcNo: int
    orgInvcNo: int
    spplrTpin: str
    spplrBhfId: str
    spplrNm: str
    spplrInvcNo: str
    regTyCd: str
    pchsTyCd: str
    rcptTyCd: str
    pmtTyCd: str
    pchsSttsCd: str
    cfmDt: str
    pchsDt: str
    cnclReqDt: str
    cnclDt: str
    totItemCnt: Decimal
    totTaxblAmt: Decimal
    totTaxAmt: Decimal
    totAmt: Decimal
    remark: str
    regrNm: str
    regrId: str
    modrNm: str
    modrId: str
    itemList: List[SavePurchase_ItemList] = field(default_factory=list)

@dataclass
class StockMaster_StockItemList:
    itemCd: str
    rsdQty: Decimal

@dataclass
class StockMaster:
    tpin: str
    bhfId: str
    regrId: str
    regrNm: str
    modrNm: str
    modrId: str
    stockItemList: List[StockMaster_StockItemList] = field(default_factory=list)

@dataclass
class CreditNoteItem:
    itemSeq: int
    itemCd: str
    itemClsCd: str
    itemNm: str
    bcd: str
    pkgUnitCd: str
    pkg: Decimal
    qtyUnitCd: str
    qty: Decimal
    prc: Decimal
    splyAmt: Decimal
    dcRt: Decimal
    dcAmt: Decimal
    isrccCd: str
    isrccNm: str
    isrcRt: Decimal
    isrcAmt: Decimal
    vatCatCd: str
    exciseTxCatCd: str
    tlCatCd: str
    iplCatCd: str
    vatTaxblAmt: Decimal
    vatAmt: Decimal
    exciseTaxblAmt: Decimal
    tlTaxblAmt: Decimal
    iplTaxblAmt: Decimal
    iplAmt: Decimal
    tlAmt: Decimal
    exciseTxAmt: Decimal
    totAmt: Decimal

@dataclass
class CreditNote:
    tpin: str
    bhfId: str
    orgSdcId: str
    orgInvcNo: int
    cisInvcNo: str
    custTpin: str
    custNm: str
    salesTyCd: str
    rcptTyCd: str
    pmtTyCd: str
    salesSttsCd: str
    cfmDt: str
    salesDt: str
    stockRlsDt: str
    cnclReqDt: str
    cnclDt: str
    rfdDt: str
    rfdRsnCd: str
    totItemCnt: int
    taxblAmtA: Decimal
    taxblAmtB: Decimal
    taxblAmtC1: Decimal
    taxblAmtC2: Decimal
    taxblAmtC3: Decimal
    taxblAmtD: Decimal
    taxblAmtRvat: Decimal
    taxblAmtE: Decimal
    taxblAmtF: Decimal
    taxblAmtIpl1: Decimal
    taxblAmtIpl2: Decimal
    taxblAmtTl: Decimal
    taxblAmtEcm: Decimal
    taxblAmtExeeg: Decimal
    taxblAmtTot: Decimal
    taxRtA: Decimal
    taxRtB: Decimal
    taxRtC1: Decimal
    taxRtC2: Decimal
    taxRtC3: Decimal
    taxRtD: Decimal
    tlAmt: Decimal
    taxRtRvat: Decimal
    taxRtE: Decimal
    taxRtF: Decimal
    taxRtIpl1: Decimal
    taxRtIpl2: Decimal
    taxRtTl: Decimal
    taxRtEcm: Decimal
    taxRtExeeg: Decimal
    taxRtTot: Decimal
    taxAmtA: Decimal
    taxAmtB: Decimal
    taxAmtC1: Decimal
    taxAmtC2: Decimal
    taxAmtC3: Decimal
    taxAmtD: Decimal
    taxAmtRvat: Decimal
    taxAmtE: Decimal
    taxAmtF: Decimal
    taxAmtIpl1: Decimal
    taxAmtIpl2: Decimal
    taxAmtTl: Decimal
    taxAmtEcm: Decimal
    taxAmtExeeg: Decimal
    taxAmtTot: Decimal
    totTaxblAmt: Decimal
    totTaxAmt: Decimal
    totAmt: Decimal
    prchrAcptcYn: str
    remark: str
    regrId: str
    regrNm: str
    modrId: str
    modrNm: str
    saleCtyCd: str
    lpoNumber: str
    currencyTyCd: str
    exchangeRt: str
    destnCountryCd: str
    dbtRsnCd: str
    invcAdjustReason: str
    itemList: List[CreditNoteItem] = field(default_factory=list)

@dataclass
class InvoiceItemNested:
    itemSeq: int
    itemCd: str
    itemClsCd: str
    itemNm: str
    bcd: str
    pkgUnitCd: str
    pkg: Decimal
    qtyUnitCd: str
    qty: Decimal
    prc: Decimal
    splyAmt: Decimal
    dcRt: Decimal
    dcAmt: Decimal
    isrccCd: str
    isrccNm: str
    isrcRt: Decimal
    isrcAmt: Decimal
    vatCatCd: str
    exciseTxCatCd: str
    tlCatCd: str
    iplCatCd: str
    vatTaxblAmt: Decimal
    vatAmt: Decimal
    exciseTaxblAmt: Decimal
    tlTaxblAmt: Decimal
    iplTaxblAmt: Decimal
    iplAmt: Decimal
    tlAmt: Decimal
    exciseTxAmt: Decimal
    totAmt: Decimal

@dataclass
class Invoice:
    tpin: str
    bhfId: str
    orgInvcNo: int
    cisInvcNo: str
    custTpin: str
    custNm: str
    salesTyCd: str
    rcptTyCd: str
    pmtTyCd: str
    salesSttsCd: str
    cfmDt: str
    salesDt: str
    stockRlsDt: str
    cnclReqDt: str
    cnclDt: str
    rfdDt: str
    rfdRsnCd: str
    totItemCnt: int
    taxblAmtA: Decimal
    taxblAmtB: Decimal
    taxblAmtC1: Decimal
    taxblAmtC2: Decimal
    taxblAmtC3: Decimal
    taxblAmtD: Decimal
    taxblAmtRvat: Decimal
    taxblAmtE: Decimal
    taxblAmtF: Decimal
    taxblAmtIpl1: Decimal
    taxblAmtIpl2: Decimal
    taxblAmtTl: Decimal
    taxblAmtEcm: Decimal
    taxblAmtExeeg: Decimal
    taxblAmtTot: Decimal
    taxRtA: Decimal
    taxRtB: Decimal
    taxRtC1: Decimal
    taxRtC2: Decimal
    taxRtC3: Decimal
    taxRtD: Decimal
    tlAmt: Decimal
    taxRtRvat: Decimal
    taxRtE: Decimal
    taxRtF: Decimal
    taxRtIpl1: Decimal
    taxRtIpl2: Decimal
    taxRtTl: Decimal
    taxRtEcm: Decimal
    taxRtExeeg: Decimal
    taxRtTot: Decimal
    taxAmtA: Decimal
    taxAmtB: Decimal
    taxAmtC1: Decimal
    taxAmtC2: Decimal
    taxAmtC3: Decimal
    taxAmtD: Decimal
    taxAmtRvat: Decimal
    taxAmtE: Decimal
    taxAmtF: Decimal
    taxAmtIpl1: Decimal
    taxAmtIpl2: Decimal
    taxAmtTl: Decimal
    taxAmtEcm: Decimal
    taxAmtExeeg: Decimal
    taxAmtTot: Decimal
    totTaxblAmt: Decimal
    totTaxAmt: Decimal
    totAmt: Decimal
    prchrAcptcYn: str
    remark: str
    regrId: str
    regrNm: str
    modrId: str
    modrNm: str
    saleCtyCd: str
    lpoNumber: str
    currencyTyCd: str
    exchangeRt: str
    destnCountryCd: str
    dbtRsnCd: str
    invcAdjustReason: str
    itemList: List[InvoiceItemNested] = field(default_factory=list)

# ==========================================
# Main Library Class
# ==========================================

class HavanoZRALib:
    def __init__(self):
        # Setup Frappe Logger
        self.logger = frappe.logger("havano_zra")
    def get_config_value(self, fieldname: str) -> str:
        try:
            doctype ="zra information"
            value = frappe.db.get_single_value(doctype, fieldname)
            return value
        except Exception as e:
            frappe.log_error(frappe.get_traceback(),f"Error fetching {fieldname} from {doctype}: {e}")
            return None
    
    
    def update_zra_information(self, fieldname: str, new_value):
        frappe.db.set_single_value("ZRA Information", fieldname, new_value)
        frappe.db.commit()

        return {
            "status": "success",
            "message": f"{fieldname} updated successfully",
            "new_value": new_value
    }
    
   
    def is_internet_available(self) -> bool:
        try:
            response = requests.get("http://www.google.com", timeout=5)
            return response.status_code == 200
        except Exception:
            return False

    def _is_result_succeeded(self, json_string: str) -> bool:
        try:
            json_obj = json.loads(json_string)
            return json_obj.get("resultMsg") == "It is succeeded"
        except Exception:
            return False

    def get_server(self) -> str:
        return self.get_config_value("zra_server_url") or ""

    
    def send_api_request(self) -> str:
        endpoint = "initializer/selectInitInfo"
        url = self.get_server() + endpoint
        
        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "dvcSrlNo": self.get_config_value("device_serial_number")
        }
        
        json_body = json.dumps(payload, indent=4)
        
        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            return response.text
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Send API Request")
            return str(e)

    def check_zra_local_server(self) -> bool:
        try:
            response = requests.get("http://www.google.com", timeout=5)
            return response.status_code == 200
        except Exception:
            return False

    def initializer_device(self) -> str:
        endpoint = "initializer/selectInitInfo"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "dvcSrlNo": self.get_config_value("device_serial_number")
        }
        
        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            if response.status_code == 200:
                json_obj = response.json()
                self.logger.info(f"Device Initialization Status: {json_obj}")
                
                res_msg = json_obj.get("resultMsg", "")
                
                if res_msg == "This device is installed":
                    return res_msg
                else:
                    res_msg = "Device Initialized"
                    req_date = json_obj.get("resultDt", "")
                    
                    data_info = json_obj.get("data", {}).get("info", {})
                    sdc_id = data_info.get("sdcId", "")
                    mrc_no = data_info.get("mrcNo", "")
                    last_pchs_invc_no = data_info.get("lastPchsInvcNo", 0)
                    last_sale_rcpt_no = data_info.get("lastSaleRcptNo", 0)
                    last_invc_no = data_info.get("lastInvcNo", "")
                    last_sale_invc_no = data_info.get("lastSaleInvcNo", 0)
                    last_train_invc_no = data_info.get("lastTrainInvcNo", "")
                    last_profrm_invc_no = data_info.get("lastProfrmInvcNo", "")
                    last_copy_invc_no = data_info.get("lastCopyInvcNo", "")

                    self.update_zra_information("resultDt", str(req_date))
                    self.update_zra_information("sdcId", str(sdc_id))
                    self.update_zra_information("mrcNo", str(mrc_no))
                    self.update_zra_information("lastPchsInvcNo", str(last_pchs_invc_no))
                    self.update_zra_information("lastSaleRcptNo", str(last_sale_rcpt_no))
                    self.update_zra_information("lastInvcNo", str(last_invc_no))
                    self.update_zra_information("lastSaleInvcNo", str(last_sale_invc_no))
                    self.update_zra_information("lastTrainInvcNo", str(last_train_invc_no))
                    self.update_zra_information("lastProfrmInvcNo", str(last_profrm_invc_no))
                    self.update_zra_information("lastCopyInvcNo", str(last_copy_invc_no))
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Initializer Device")

        return res_msg

    def get_standard_codes(self) -> str:
        endpoint = "code/selectCodes"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
             "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "lastReqDt": self.get_config_value("result_date")
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                self.logger.info(f"Standard Code Req. Status: {json_obj}")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Standard Codes")
        
        return res_msg

    def get_notices(self) -> str:
        endpoint = "notices/selectNotices"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "lastReqDt": self.get_config_value("result_date")
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                self.logger.info(f"Notice Status: {json_obj}")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Notices")
        
        return res_msg

    def save_item_cls_data(self, json_string: str):
        # In Frappe, file operations in site path are valid
        try:
            site_path = frappe.get_site_path("zraitemclass.dat")
        except:
            site_path = os.path.join(os.getcwd(), "zraitemclass.dat")

        try:
            data = json.loads(json_string)
            
            if data is None or data.get("data") is None or data["data"].get("itemClsList") is None:
                frappe.log_error(f"Havano ZRA Log",f"Invalid JSON structure or missing itemClsList.")
                
                return

            with open(site_path, 'w') as writer:
                for item in data["data"]["itemClsList"]:
                    if item.get("itemClsCd") and item.get("itemClsNm"):
                        writer.write(f"{item['itemClsCd']} - {item['itemClsNm']}\n")
        except Exception as ex:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Save Item Class Data")

    def get_class_code(self) -> str:
        endpoint = "itemClass/selectItemsClass"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
           "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "lastReqDt": self.get_config_value("result_date")
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                self.save_item_cls_data(res_msg)
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Get Class Code Req. Status: {json_obj}")
                
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Get Class Code Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Class Code")

        return res_msg

    def get_customer_info(self, cus_tpin: str) -> str:
        endpoint = "customers/selectCustomer"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
           "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "custmTpin": cus_tpin
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Get Customer Req. Status: {json_obj}")
                
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Get Customer Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Customer")

        return res_msg

    def save_branch_user(self, user_id: str, user_name: str, user_address: str, active_status: bool, 
                                branch_user_creator_username: str, branch_user_creator_userID: str, 
                                modifier_username: str, modifier_userID: str) -> str:
        endpoint = "branches/saveBrancheUser"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "userId": user_id,
            "userNm": user_name,
            "adrs": user_address,
            "useYn": active_status,
            "regrNm": branch_user_creator_username,
            "regrId": branch_user_creator_userID,
            "modrNm": modifier_username,
            "modrId": modifier_username
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Save Branch User Req. Status: {json_obj}")
                
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Save Branch User Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Save Branch User")

        return res_msg

    def get_branches(self) -> str:
        endpoint = "branches/selectBranches"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "lastReqDt": self.get_config_value("result_date")
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Get Branches Req. Status: {json_obj}")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Branches")

        return res_msg

    def save_branch_customers(self, customer_mobileno: str, customer_tpin: str, customer_name: str, 
                                    customer_address: str, customer_email: str, customer_faxno: str,
                                    active_status: bool, remark: str, creator_username: str, 
                                    creator_userID: str, modifier_username: str, modifier_userID: str) -> str:
        endpoint = "branches/saveBrancheUser"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "custNo": customer_mobileno,
            "custTpin": customer_tpin,
            "custNm": customer_name, 
            "Adrs": customer_address,
            "Email": customer_email,
            "faxNo": customer_faxno,
            "remark": remark,
            "regrNm": creator_username,
            "regrId": creator_userID,
            "modrNm": modifier_username,
            "modrId": modifier_username
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                self.logger.info(f"Save Branch Customers Req. Status: {json_obj}")
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Save Branch Customers Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Save Branch Customers")

        return res_msg

    def save_item(self, item_code: str, item_class_code: str, item_type_code: str, item_name: str, 
                        item_standard_name: str, origin_country_code: str, packaging_unitCode: str, 
                        qty_unit_code: str, vat_category_code: str, ipl_cat_code: str, tl_cat_code: str, 
                        excess_tax_cat_code: str, branch_no: str, barcode: str, unit_price: str, 
                        additional_info: str, safety_qty: str, insurance_applicable: str, active_status: str,
                        creator_username: str, creator_userID: str, modifier_username: str, modifier_userID: str) -> str:
        endpoint = "items/saveItem"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
           "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "itemCd": item_code,
            "itemClsCd": item_class_code,
            "itemTyCd": item_type_code,
            "itemNm": item_name,
            "itemStdNm": item_standard_name,
            "orgnNatCd": origin_country_code,
            "pkgUnitCd": packaging_unitCode,
            "qtyUnitCd": qty_unit_code,
            "vatCatCd": vat_category_code,
            "iplCatCd": ipl_cat_code,
            "tlCatCd": tl_cat_code,
            "exciseTxCatCd": excess_tax_cat_code,
            "btchNo": branch_no,
            "bcd": barcode,
            "dftPrc": f"{Decimal(unit_price):.2f}",
            "addInfo": additional_info,
            "sftyQty": safety_qty,
            "isrcAplcbYn": insurance_applicable,
            "useYn": active_status,
            "regrNm": creator_username,
            "regrId": creator_userID,
            "modrNm": modifier_username,
            "modrId": modifier_username
        }

        json_body = json.dumps(payload, indent=4)
        print(json_body)
        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            
            # Logic: check if succeeded
            json_obj = response.json()
            res_msg = response.text
            
            if response.status_code == 200:
                if self._is_result_succeeded(json.dumps(json_obj)):
                    print(json_obj)
                    req_date = json_obj.get("resultDt", "")
                    if req_date != "":
                        self.update_zra_information("resultDt", str(req_date))
                    frappe.log_error(f"Havano ZRA Log",f"Save Item Req. Status: {json_obj}")
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Save Item Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Save Item")

        return res_msg

    def update_item(self, item_code: str, item_class_code: str, item_type_code: str, item_name: str, 
                        item_standard_name: str, origin_country_code: str, packaging_unitCode: str, 
                        qty_unit_code: str, vat_category_code: str, ipl_cat_code: str, tl_cat_code: str, 
                        excess_tax_cat_code: str, branch_no: str, barcode: str, unit_price: str, 
                        additional_info: str, safety_qty: str, insurance_applicable: str, active_status: str,
                        creator_username: str, creator_userID: str, modifier_username: str, modifier_userID: str) -> str:
        endpoint = "items/updateItem"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
           "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "itemCd": item_code,
            "itemClsCd": item_class_code,
            "itemTyCd": item_type_code,
            "itemNm": item_name,
            "itemStdNm": item_standard_name,
            "orgnNatCd": origin_country_code,
            "pkgUnitCd": packaging_unitCode,
            "qtyUnitCd": qty_unit_code,
            "vatCatCd": vat_category_code,
            "iplCatCd": ipl_cat_code,
            "tlCatCd": tl_cat_code,
            "exciseTxCatCd": excess_tax_cat_code,
            "btchNo": branch_no,
            "bcd": barcode,
            "dftPrc": f"{Decimal(unit_price):.2f}",
            "addInfo": additional_info,
            "sftyQty": safety_qty,
            "isrcAplcbYn": insurance_applicable,
            "useYn": active_status,
            "regrNm": creator_username,
            "regrId": creator_userID,
            "modrNm": modifier_username,
            "modrId": modifier_username
        }

        json_body = json.dumps(payload, indent=4)
        print(json_body)
        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            
            # Logic: check if succeeded
            json_obj = response.json()
            res_msg = response.text
            
            if response.status_code == 200:
                if self._is_result_succeeded(json.dumps(json_obj)):
                    print(json_obj)
                    req_date = json_obj.get("resultDt", "")
                    if req_date != "":
                        self.update_zra_information("resultDt", str(req_date))
                    frappe.log_error(f"Havano ZRA Log",f"Update Item Req. Status: {json_obj}")
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Save Item Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Update Item")

        return res_msg
    
    def get_items(self) -> str:
        endpoint = "items/selectItems"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "lastReqDt": self.get_config_value("result_date")
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Get Items Req. Status: {json_obj}")
                
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Get Items Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Items")

        return res_msg

    def get_item(self, item_code: str) -> str:
        endpoint = "items/selectItem"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "itemCd": item_code
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Get Items Req. Status: {json_obj}")
                
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Get Item Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Get Item")

        return res_msg

    def save_composition_item(self, item_code: str, composition_item_code: str, composition_qty: str, 
                                   creator_username: str, creator_userID: str) -> str:
        endpoint = "items/saveItem"
        res_msg = ""
        url = self.get_server() + endpoint

        payload = {
            "tpin": self.get_config_value("tpin"),
            "bhfId": self.get_config_value("branch_id"),
            "itemCd": item_code,
            "cpstItemCd": composition_item_code,
            "cpstQty": composition_qty,
            "regrNm": creator_username,
            "regrId": creator_userID
        }

        json_body = json.dumps(payload, indent=4)

        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            res_msg = response.text
            if response.status_code == 200:
                json_obj = response.json()
                req_date = json_obj.get("resultDt", "")
                if req_date != "":
                    self.update_zra_information("resultDt", str(req_date))
                frappe.log_error(f"Havano ZRA Log",f"Save Composition Item Req. Status:  {json_obj}")
                
            else:
                 frappe.log_error(f"Status Code: {response.status_code} - {response.text}", "Havano ZRA: Save Composition Item Error")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA: Save Composition Item")

        return res_msg

    def send_invoice(self, cis_invoice_no: str, customer_tpin: str, customer_name: str, 
                           total_item_count: int, remark: str, creator_username: str, creator_user_id: str, 
                           modifier_username: str, modifier_user_id: str, lpo_number: str, currency_code: str, 
                           exchange_rate: str, destn_country_code: str, items_xml: str) -> str:
        
        tpin = self.get_config_value("tpin")
        branch_id = self.get_config_value("branch_id")
        sales_type_code = "N"
        receipt_type_code = "S"
        payment_type_code = "01"
        sales_status_code = "02"
        
        from datetime import datetime
        now = datetime.now()
        confirm_date = now.strftime("%Y%m%d%H%M%S")
        sales_date = now.strftime("%Y%m%d")
        stock_release_date = None
        cancel_request_date = None
        cancel_date = None
        refund_date = None
        refund_reason = None
        
        total_item_count_val = 0 
        
        taxable_amt_a = Decimal('0')
        taxable_amt_b = Decimal('0')
        taxable_amt_c1 = Decimal('0')
        taxable_amt_c2 = Decimal('0')
        taxable_amt_c3 = Decimal('0')
        taxable_amt_d = Decimal('0')
        taxable_amt_rvat = Decimal('0')
        taxable_amt_e = Decimal('0')
        taxable_amt_f = Decimal('0')
        taxable_amt_ipl1 = Decimal('0')
        taxable_amt_ipl2 = Decimal('0')
        taxable_amt_tl = Decimal('0')
        taxable_amt_ecm = Decimal('0')
        taxable_amt_exeeg = Decimal('0')
        taxable_amt_tot = Decimal('0')
        
        tax_rate_a = Decimal('16')
        tax_rate_b = Decimal('16')
        tax_rate_c1 = Decimal('0')
        tax_rate_c2 = Decimal('0')
        tax_rate_c3 = Decimal('0')
        tax_rate_d = Decimal('0')
        tax_rate_rvat = Decimal('16')
        tax_rate_e = Decimal('0')
        tax_rate_f = Decimal('10')
        tax_rate_ipl1 = Decimal('5')
        tax_rate_ipl2 = Decimal('0')
        tax_rate_tl = Decimal('1.5')
        tax_rate_ecm = Decimal('5')
        tax_rate_exeeg = Decimal('3')
        tax_rate_tot = Decimal('0')
        
        tax_amount_a = Decimal('0')
        tax_amount_b = Decimal('0')
        tax_amount_c1 = Decimal('0')
        tax_amount_c2 = Decimal('0')
        tax_amount_c3 = Decimal('0')
        tax_amount_d = Decimal('0')
        tax_amount_rvat = Decimal('0')
        tax_amount_e = Decimal('0')
        tax_amount_f = Decimal('0')
        tax_amount_ipl1 = Decimal('0')
        tax_amount_ipl2 = Decimal('0')
        tax_amount_tl = Decimal('0')
        tax_amount_ecm = Decimal('0')
        tax_amount_exeeg = Decimal('0')
        tax_amount_tot = Decimal('0')
        
        tot_taxbl_amount = Decimal('0')
        tot_tax_amount = Decimal('0')
        tot_amount = Decimal('0')
        
        purchase_acceptance_yn = "Y"
        sale_city_cd = "1"
        debit_reason_code = None
        invoice_adjustment_reason = None

        item_list = []

        try:
            root = ET.fromstring(items_xml)
            item_nodes = root.findall("ITEM") 
            
            for item_node in item_nodes:
                total_item_count_val += 1
                
                def get_text(tag):
                    el = item_node.find(tag)
                    return el.text if el is not None else ""

                seq_no = int(get_text("ItemSeq"))
                item_code_node = get_text("ItemCd")
                item_class_code = get_text("ItemClsCd")
                item_name = get_text("ItemNm")
                barcode = get_text("Bcd")
                pkg_unit_code = get_text("PkgUnitCd")
                package = int(get_text("Pkg"))
                qty_unit_code = get_text("QtyUnitCd")
                qty = Decimal(get_text("Qty"))
                price = Decimal(get_text("Prc"))
                supply_amount = Decimal(get_text("SplyAmt"))
                discount_rate = Decimal(get_text("DcRt"))
                discount_amount = Decimal(get_text("DcAmt"))
                insurance_company_code = get_text("IsrccCd")
                insurance_company_name = get_text("IsrccNm")
                insurance_company_rate = Decimal(get_text("IsrcRt"))
                insurance_amount = Decimal(get_text("IsrcAmt"))
                vat_category_code = get_text("VatCatCd")
                excise_tax_cat_code = get_text("ExciseTxCatCd")
                tl_cat_code = get_text("TlCatCd")
                ipl_cat_code = get_text("IplCatCd")
                vat_taxbl_amt = Decimal(get_text("VatTaxblAmt"))
                vat_amt = Decimal(get_text("VatAmt"))
                excise_taxbl_amt = Decimal(get_text("ExciseTaxblAmt"))
                tl_taxbl_amt = Decimal(get_text("TlTaxblAmt"))
                ipl_taxbl_amt = Decimal(get_text("IplTaxblAmt"))
                ipl_amt = Decimal(get_text("IplAmt"))
                tl_amt = Decimal(get_text("TlAmt"))
                excise_tx_amt = Decimal(get_text("ExciseTxAmt"))
                tot_amount_item = Decimal(get_text("TotAmt"))

                tot_amount += tot_amount_item
                
                if vat_category_code == "A":
                    taxable_amt_a += vat_taxbl_amt
                    tax_amount_a += vat_amt
                    tot_taxbl_amount += vat_taxbl_amt
                    tot_tax_amount += vat_amt
                
                if vat_category_code == "B":
                    taxable_amt_b += vat_taxbl_amt
                    tax_amount_b += vat_amt
                    tot_taxbl_amount += vat_taxbl_amt
                    tot_tax_amount += vat_amt

                if vat_category_code == "C1":
                    taxable_amt_c1 += vat_taxbl_amt
                    tax_amount_c1 += vat_amt
                    tot_taxbl_amount += vat_taxbl_amt

                if vat_category_code == "C2":
                    taxable_amt_c2 += vat_taxbl_amt
                    tax_amount_c2 += vat_amt
                    tot_taxbl_amount += vat_taxbl_amt

                if vat_category_code == "C3":
                    taxable_amt_c3 += vat_taxbl_amt
                    tax_amount_c3 += vat_amt
                    tot_taxbl_amount += vat_taxbl_amt

                itm = InvoiceItemNested(
                    itemSeq=seq_no,
                    itemCd=item_class_code, 
                    itemClsCd=item_class_code,
                    itemNm=item_name,
                    bcd=barcode,
                    pkgUnitCd=pkg_unit_code,
                    pkg=Decimal(package), 
                    qtyUnitCd=qty_unit_code,
                    qty=qty,
                    prc=price,
                    splyAmt=supply_amount,
                    dcRt=discount_rate,
                    dcAmt=discount_amount,
                    isrccCd=insurance_company_code,
                    isrccNm=insurance_company_name,
                    isrcRt=insurance_company_rate,
                    isrcAmt=insurance_amount,
                    vatCatCd=vat_category_code,
                    exciseTxCatCd=excise_tax_cat_code,
                    tlCatCd=tl_cat_code,
                    iplCatCd=ipl_cat_code,
                    vatTaxblAmt=vat_taxbl_amt,
                    vatAmt=vat_amt,
                    exciseTaxblAmt=excise_taxbl_amt,
                    tlTaxblAmt=tl_taxbl_amt,
                    iplTaxblAmt=ipl_taxbl_amt,
                    iplAmt=ipl_amt,
                    tlAmt=tl_amt,
                    exciseTxAmt=excise_tx_amt,
                    totAmt=tot_amount_item
                )
                item_list.append(itm)

            invoice = Invoice(
                tpin=tpin,
                bhfId=branch_id,
                orgInvcNo=0,
                cisInvcNo=cis_invoice_no,
                custTpin=customer_tpin,
                custNm=customer_name,
                salesTyCd=sales_type_code,
                rcptTyCd=receipt_type_code,
                pmtTyCd=payment_type_code,
                salesSttsCd=sales_status_code,
                cfmDt=confirm_date,
                salesDt=sales_date,
                stockRlsDt=stock_release_date,
                cnclReqDt=cancel_request_date,
                cnclDt=cancel_date,
                rfdDt=refund_date,
                rfdRsnCd=refund_reason,
                totItemCnt=total_item_count_val,
                taxblAmtA=taxable_amt_a,
                taxblAmtB=taxable_amt_b,
                taxblAmtC1=taxable_amt_c1,
                taxblAmtC2=taxable_amt_c2,
                taxblAmtC3=taxable_amt_c3,
                taxblAmtD=taxable_amt_d,
                taxblAmtRvat=taxable_amt_rvat,
                taxblAmtE=taxable_amt_e,
                taxblAmtF=taxable_amt_f,
                taxblAmtIpl1=taxable_amt_ipl1,
                taxblAmtIpl2=taxable_amt_ipl2,
                taxblAmtTl=taxable_amt_tl,
                taxblAmtEcm=taxable_amt_ecm,
                taxblAmtExeeg=taxable_amt_exeeg,
                taxblAmtTot=taxable_amt_tot,
                taxRtA=tax_rate_a,
                taxRtB=tax_rate_b,
                taxRtC1=tax_rate_c1,
                taxRtC2=tax_rate_c2,
                taxRtC3=tax_rate_c3,
                taxRtD=tax_rate_d,
                tlAmt=Decimal('0'), 
                taxRtRvat=tax_rate_rvat,
                taxRtE=tax_rate_e,
                taxRtF=tax_rate_f,
                taxRtIpl1=tax_rate_ipl1,
                taxRtIpl2=tax_rate_ipl2,
                taxRtTl=tax_rate_tl,
                taxRtEcm=tax_rate_ecm,
                taxRtExeeg=tax_rate_exeeg,
                taxRtTot=tax_rate_tot,
                taxAmtA=tax_amount_a,
                taxAmtB=tax_amount_b,
                taxAmtC1=tax_amount_c1,
                taxAmtC2=tax_amount_c2,
                taxAmtC3=tax_amount_c3,
                taxAmtD=tax_amount_d,
                taxAmtRvat=tax_amount_rvat,
                taxAmtE=tax_amount_e,
                taxAmtF=tax_amount_f,
                taxAmtIpl1=tax_amount_ipl1,
                taxAmtIpl2=tax_amount_ipl2,
                taxAmtTl=tax_amount_tl,
                taxAmtEcm=tax_amount_ecm,
                taxAmtExeeg=tax_amount_exeeg,
                taxAmtTot=tax_amount_tot,
                totTaxblAmt=tot_taxbl_amount,
                totTaxAmt=tot_tax_amount,
                totAmt=tot_amount,
                prchrAcptcYn=purchase_acceptance_yn,
                remark=remark,
                regrId=creator_user_id,
                regrNm=creator_username,
                modrId=modifier_user_id,
                modrNm=modifier_username,
                saleCtyCd=sale_city_cd,
                lpoNumber=lpo_number,
                currencyTyCd=currency_code,
                exchangeRt=exchange_rate,
                destnCountryCd=destn_country_code,
                dbtRsnCd=debit_reason_code,
                invcAdjustReason=invoice_adjustment_reason,
                itemList=item_list
            )
            
            def serialize_invoice(inv: Invoice) -> dict:
                d = {}
                for k, v in inv.__dict__.items():
                    if isinstance(v, Decimal):
                        d[k] = str(v)
                    elif isinstance(v, list):
                        d[k] = [serialize_invoice_item(i) for i in v]
                    else:
                        d[k] = v
                return d

            def serialize_invoice_item(item: InvoiceItemNested) -> dict:
                d = {}
                for k, v in item.__dict__.items():
                    if isinstance(v, Decimal):
                        d[k] = str(v)
                    else:
                        d[k] = v
                return d

            json_body = serialize_invoice(invoice)
            #payload = json.dumps(json_body, indent=4) 
            payload = json_body
            endpoint = "trnsSales/saveSales"
            
            url = self.get_server() + endpoint
            print(url)
            print(payload)
            #return ""
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            
            if response.status_code != 200:
                frappe.log_error(f"Havano ZRA Success Status: {response.status_code}\nResponse: {response.text}", "Havano ZRA: Send Invoice Failed")
            
            return response.text

        except ET.ParseError as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA Error Log: Send Invoice XML Parse Error")
            return ""
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Havano ZRA Error Log: Send Invoice Error")
            return ""
