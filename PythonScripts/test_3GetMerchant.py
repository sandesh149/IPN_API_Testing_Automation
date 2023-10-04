import json
import requests
import test_1ipncred
import time
#verifyMer = test_CreateMerchant.verifyMer


cookies = test_1ipncred.cookies
getMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/list?page=0"
response_getmer = requests.get(getMer, cookies=cookies)
st_codeGMer = response_getmer.status_code

json_response_getmer = response_getmer.json()
if st_codeGMer == 200:
    #print(json_response_getmer)
    #print(json_response_getmer["data"])
    noofmer = len(list(json_response_getmer["data"]))
    print(noofmer)
    if noofmer > 0:
        #print(json_response_getmer["data"])
        merchantid = json_response_getmer["data"][0].get("id")
        print(merchantid)
    #print(noofmer)
    def test_status_code_getMerchant():
        assert st_codeGMer == 200, "Status code received is " + str(st_codeGMer)
    def test_isListEmpty():
        assert noofmer > 0, " Merchant List is empty."
else:
    def test_status_code_getMerchant():
        assert st_codeGMer == 200, "Expected status code 200, got " + str(st_codeGMer)



