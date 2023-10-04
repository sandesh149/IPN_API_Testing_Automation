import json
import requests
import test_1ipncred
import test_2CreateMerchant
import test_3GetMerchant

print(" Doing getmerchant by id")
try:
    getmer = test_2CreateMerchant.getmer
except:
    getmer = "No"
#merchantID = ""
idmer = test_3GetMerchant.merchantid
location = test_1ipncred.location
if getmer == "Yes":
    cookies = test_1ipncred.cookies
    #idMer = test_2CreateMerchant.merid
    with open(location + 'createMer.json','r') as cmerfile:
        createMer_input = cmerfile.read()

    request_json_cmer = json.loads(createMer_input)

    getidMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/get/"+ str(idmer)
    response_idmer = requests.get(getidMer, cookies=cookies)
    st_codeGMer = response_idmer.status_code
    json_response_getidmer = response_idmer.json()
    checkStatus = json_response_getidmer.get("status")
    print(checkStatus)
    if st_codeGMer == 200:

        #print(json_response_getidmer["data"])
        def test_status_code_getIDMerchant():
            assert st_codeGMer == 200, "Status code received is " + str(st_codeGMer)

        def test_checkStatus():
            assert checkStatus == "success", "Status received: " + checkStatus

        def test_isResEmpty():
            assert json_response_getidmer["message"] == "retrieved" , "Merchant Id not found."
            print(json_response_getidmer["message"])
        def test_checkEmail():
            assert json_response_getidmer["data"]["email"] == request_json_cmer["data"]["email"], "Expected: " + request_json_cmer["data"]["email"] +"  Got: "+ json_response_getidmer["data"]["email"]

        def test_checkPhone():
            assert json_response_getidmer["data"]["phone"] == request_json_cmer["data"]["phone"], "Expected: " + request_json_cmer["data"]["phone"] + "  Got: " +json_response_getidmer["data"]["phone"]

        def test_checkPan():
            assert json_response_getidmer["data"]["pan"] == request_json_cmer["data"]["pan"], "Expected: " + request_json_cmer["data"]["pan"] + "  Got: " + json_response_getidmer["data"]["pan"]

        def test_checkAcNumber():
            assert json_response_getidmer["data"]["account_number"] == request_json_cmer["data"]["account_number"], "Expected: " + request_json_cmer["data"]["account_number"] + "  Got: " + json_response_getidmer["data"]["account_number"]



    else:
        def test_status_code_getIDMerchant():
            assert st_codeGMer == 200, "Expected status code 200, got " + str(st_codeGMer)
        def test_checkStatus():
            assert checkStatus == "success", "Status received: " + checkStatus

print("  getmerchant by id complete")