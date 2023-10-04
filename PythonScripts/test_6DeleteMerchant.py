import json
import requests
import test_1ipncred
import test_3GetMerchant
import time


cookies = test_1ipncred.cookies
location = test_1ipncred.location
deleteMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/delete"



delid =test_3GetMerchant.merchantid
request_json_delmer = {"merchant_id": delid}
        #print(request_json_delmer)
response_delmer = requests.post(deleteMer, json=request_json_delmer, cookies=cookies)
st_codeDelmer = response_delmer.status_code
json_response_delmer = response_delmer.json()
        #print(json_response_delmer)
checkStatus = json_response_delmer["status"]
        #print(checkStatus)

if st_codeDelmer == 200:

    def test_status_code_deleteMerchant():
        assert st_codeDelmer == 200, "Status code received is " + str(st_codeDelmer)
    def test_checkdelStatus():
        assert checkStatus == "success", "Merchant del failed."


    if checkStatus == "success":

        with open(location + 'verifyMer.json','w') as vmerfile:
                # VMer_input = vmerfile.read()
                dict = {
                    "request_id": int(json_response_delmer["data"].get("id")),
                    "action": "APPROVE"
                }
                json.dump(dict, vmerfile)

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
                    if resstatus == "success" and checkApprove == "APPROVED":
                        getidMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/get/" + str(delid)
                        response_idmer = requests.get(getidMer, cookies=cookies)
                        st_codeGMer = response_idmer.status_code
                        json_response_getidmer = response_idmer.json()

                        def checkStcodeafterdelverify(self):
                            assert self.st_codeGMer == 404, "Expected 404, got "+ self.st_codeGMer
                        def checkMessage(self):
                            assert self.json_response_getidmer.get("message") == "merchant not found", "Merchant not deleted"
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
        print("done verification")
else:
    def test_status_code_deleteMerchant():
        assert st_codeDelmer != 200, "Status code received is " + str(st_codeDelmer)
    def test_checkdelStatus():
        assert checkStatus == "success", "Merchant del failed."
