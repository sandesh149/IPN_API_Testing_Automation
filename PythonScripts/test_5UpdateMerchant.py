import json
import requests
import test_1ipncred
import  test_3GetMerchant
import time



print( "Doinf for update")
location = test_1ipncred.location
cookies = test_1ipncred.cookies
merchantId = test_3GetMerchant.merchantid
updateMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/update"

# with open(location + 'updateMer.json','w') as upfile:
#     writeMerid = upfile.read()
#     init_json = json.loads(writeMerid)
#     init_json["merchant_id"] = merchantId
#     json.dump(init_json, upfile)


with open(location + 'updateMer.json','r') as upfile:
    updateMer_input = upfile.read()
request_json_umer = json.loads(updateMer_input)
request_json_umer["merchant_id"] = merchantId

print(request_json_umer)
with open(location + 'updateMer.json','w') as upfile1:
    json.dump(request_json_umer, upfile1)

with open(location + 'updateMer.json','r') as upfile2:
    newMer_input = upfile2.read()
json_newmer = json.loads(newMer_input)
response_umer = requests.post(updateMer, json=json_newmer, cookies=cookies)
st_codeUmer = response_umer.status_code

json_response_umer = response_umer.json()
#print(json_response_umer)
checkStatus = json_response_umer["status"]
#print(checkStatus)
def test_request_email():
    assert json_newmer["data"]["email"] != "", "Email field is empty"
def test_request_phone():
    assert json_newmer["data"]["phone"] != "", "Phone field is empty"
def test_request_pan():
    assert json_newmer["data"]["pan"] != "", "PAN field is empty"
def test_request_account_number():
    assert json_newmer["data"]["account_number"] != "", "Account number field is empty"


if st_codeUmer == 200 :

    def test_status_code_updateMerchant():
        assert st_codeUmer == 200, "Status code received is " + str(st_codeUmer)
    def test_checkStatus():
        assert checkStatus == "success", "Merchant update failed."
    print(checkStatus)
    if checkStatus == "success":

        with open('C:\\Users\\sandesh.kafle\\Documents\\UiPath\\Bitskraft_IPN\\Input\\verifyMer.json', 'w') as vmerfile:
                #VMer_input = vmerfile.read()
                dict = {
                     "request_id" : int(json_response_umer["data"].get("id")),
                     "action" : "APPROVE"
                }
                json.dump(dict, vmerfile)
        print("now do for verification ater update")

        class verifyCheck:
            print("inside verifycheck")
            verMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/verify"
            with open(location + 'verifyMer.json', 'r') as vmerfile:
                verMer_input = vmerfile.read()
                request_json_vmer = json.loads(verMer_input)
            response_vmer = requests.post(verMer, json=request_json_vmer, cookies=cookies)
            print(response_vmer)
            st_codeVMer = response_vmer.status_code
            json_response_vmer = response_vmer.json()
            print(st_codeVMer)
            if st_codeVMer == 200:

                # print(json_response_vmer)
                resstatus = json_response_vmer.get("status")
                checkApprove = json_response_vmer["data"].get("status")
                print(checkApprove)

                def test_status_code_verifyMerchant(self):
                    assert self.st_codeVMer == 200, "Status code received is " + str(self.st_codeVMer)

                def test_checkstaus(self):
                    assert self.resstatus == "success", " Expected success but got " + self.resstatus

                def test_checkApprove(self):
                    assert self.checkApprove == "APPROVED", "Expected approved but got " + self.checkApprove
                if checkApprove == "APPROVED":
                    newres = json_response_vmer["data"]["new_data"]

                    def test_updatedemail(self):
                        assert self.newres.get("email") == json_newmer["data"]["email"] , "Expected: " + json_newmer["data"]["email"] + "  .Got: " + self.newres.get("email")

                    def test_updatedphone(self):
                        assert self.newres.get("phone") == json_newmer["data"]["phone"] , "Expected: " + json_newmer["data"]["phone"] + "  .Got: " + self.newres.get("phone")

                    def test_updatedpan(self):
                        assert self.newres.get("pan") == json_newmer["data"]["pan"] , "Expected: " + json_newmer["data"]["pan"] + "  .Got: " + self.newres.get("pan")

                    def test_updatedacno(self):
                        assert self.newres.get("account_number") == json_newmer["data"]["account_number"] , "Expected: " + json_newmer["data"]["account_number"] + "  .Got: " + self.newres.get("account_number")

            else:


                def test_status_code_verifyMerchant(self):
                    assert self.st_codeVMer == 200, "Status code received is " + str(self.st_codeVMer)

                if "message" in json_response_vmer:
                    resstatus = json_response_vmer.get("status")
                    def test_verMerchant(self):
                        assert self.resstatus == "success", self.json_response_vmer.get("message")

                if "detail" in json_response_vmer:
                    detail = json_response_vmer.get("detail")
                    def test_IsMerIdEmpty(self):
                        assert self.detail == "", self.detail

        verifyCheck()

else:
    def test_status_code_updateMerchant():
        assert st_codeUmer == 200, "Status code received is " + str(st_codeUmer)
    if "data" in json_response_umer["message"]:
        def test_emailFormat():
            assert json_response_umer["message"]["data"].get("email") == "" ,"Invalid email format: " + json_newmer["data"]["email"]
    else:
        def test_checkupdateStatus():
            assert checkStatus == "success", "Merchant update failed."

