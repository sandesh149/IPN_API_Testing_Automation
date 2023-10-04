import json
import requests
import test_1ipncred



createMerchant = test_1ipncred.createMerchant
location = test_1ipncred.location
if createMerchant == "Yes":
    nonempty = "No"
    cookies = test_1ipncred.cookies
    createMer = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/merchant/create"
    with open(location + 'createMer.json', 'r') as cmerfile:
        createMer_input = cmerfile.read()

    request_json_cmer = json.loads(createMer_input)
    reqdata = request_json_cmer["data"]
    response_cmer = requests.post(createMer, json=request_json_cmer, cookies=cookies)
        # print(response1.request.body)
    st_codeCMer = response_cmer.status_code

    json_response_cmer = response_cmer.json()
        # print(json_response_cmer)

    keys_list = ['email', 'phone', 'pan', 'account_number']
    keystr = " ".join(str(x) for x in keys_list).replace(" ", ",")
        # print(keystr)

    if request_json_cmer["data"].get("email") == "":
        def test_emptyrequestEmail():
            assert request_json_cmer["data"].get("email") != "", "This field may not be blank."
        nonempty = "Yes"
    else:
        if "@" in request_json_cmer["data"].get("email"):
            mailformat = "correct"
        else:
            def test_emailFormat():
                assert "@" in request_json_cmer["data"].get("email"), "Wrong email format"
            mailformat = "wrong"
    if request_json_cmer["data"].get("phone") == "":
        def test_emptyrequestPhone():
            assert request_json_cmer["data"].get("phone") != "", "This field may not be blank."
        nonempty = "Yes"
    if request_json_cmer["data"].get("pan") == "":
        def test_emptyrequestPAN():
            assert request_json_cmer["data"].get("pan") != "", "This field may not be blank."
        nonempty = "Yes"
    if request_json_cmer["data"].get("account_number") == "":
        def test_emptyrequestAcNo():
            assert request_json_cmer["data"].get("account_number") != "", "This field may not be blank."
        nonempty = "Yes"
    if st_codeCMer != 200 and nonempty == "No":
        responsedata = json_response_cmer["message"]["data"]

        def test_status_code_createMerchant():  # use test in fuction name so that it can be recognised by pytest.
            assert st_codeCMer == 200, "Status code received is " + str(st_codeCMer)

        def test_isrequestBodyEmpty():
            assert request_json_cmer["data"] != None, "Request is not empty"

        def test_isresponsebodyEmpty():
            assert responsedata != None, "Response body is empty."

        if mailformat == "correct":
            def test_checkKeys():
                responsekeys = list(responsedata.keys())
                resstr = " ".join(str(x) for x in responsekeys).replace(" ", ",")
                assert all(x in list(responsedata.keys()) for x in keys_list), "While creating Merchant, expected keys " + keystr + ".Got keys " + resstr

            if "email" in responsedata:
                def test_checkEmail():
                    resvalue = " ".join(str(x) for x in responsedata['email'])
                    assert responsedata.get('email') == reqdata.get('email'), "Expected: " + reqdata.get('email') + " .Got: " + resvalue
            if "phone" in responsedata:
                def test_checkPhone():
                    resvalue = " ".join(str(x) for x in responsedata['phone'])
                    assert responsedata.get('phone') == reqdata.get('phone'), "Expected: " + reqdata.get('phone') + " .Got: " + resvalue

            if "pan" in responsedata:
                def test_checkPan():
                    resvalue = " ".join(str(x) for x in responsedata['pan'])
                    assert responsedata.get('pan') == reqdata.get('pan'), "Expected: " + reqdata.get('pan') + " .Got: " + resvalue
            if "account_number" in responsedata:
                def test_account_no():
                    resvalue = " ".join(str(x) for x in responsedata['account_number'])
                    assert responsedata.get('account_number') == reqdata.get('account_number'), "Expected: " + reqdata.get('account_number') + " .Got: " + resvalue

            getmer = "No"
    else:
        responsedata = json_response_cmer["data"]["new_data"]



        def test_status_code_createMerchant():  # use test in fuction name so that it can be recognised by pytest.
            assert st_codeCMer == 200, "Status code received is " + str(st_codeCMer)

        def test_isrequestBodyEmpty():
            assert request_json_cmer["data"] != None, "Request is not empty"

        def test_isresponsebodyEmpty():
            assert responsedata != None, "Response body is empty."

        def test_checkKeys():
            responsekeys = list(responsedata.keys())
            resstr = " ".join(str(x) for x in responsekeys).replace(" ", ",")
            # print(resstr)
            assert all(x in list(responsedata.keys()) for x in keys_list), "While creating Merchant, expected keys " + keystr + ".Got keys " + resstr

        def test_checkEmail():
            resvalue = " ".join(str(x) for x in responsedata['email'])
            assert responsedata.get('email') == reqdata.get('email'), "Expected: " + reqdata.get('email') + " .Got: " + resvalue

        def test_checkPhone():
            resvalue = " ".join(str(x) for x in responsedata['phone'])
            assert responsedata.get('phone') == reqdata.get('phone'), "Expected: " + reqdata.get('phone') + " .Got: " + resvalue

        def test_checkPan():
            resvalue = " ".join(str(x) for x in responsedata['pan'])
            assert responsedata.get('pan') == reqdata.get('pan'), "Expected: " + reqdata.get('pan') + " .Got: " + resvalue

        def test_account_no():
            resvalue = " ".join(str(x) for x in responsedata['account_number'])
            assert responsedata.get('account_number') == reqdata.get('account_number'), "Expected: " + reqdata.get('account_number') + " .Got: " + resvalue

        def test_check_Status():
            assert json_response_cmer["status"] == "success", "Merchant creation failed."
        merid = json_response_cmer["data"]["id"]
        with open('C:\\Users\\sandesh.kafle\\Documents\\UiPath\\Bitskraft_IPN\\Input\\verifyMer.json','w') as vmerfile:
            # VMer_input = vmerfile.read()
            dict = {
                "request_id": merid,
                "action": "APPROVE"
            }
            json.dump(dict, vmerfile)


        class verifyCheck:

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
                    assert self.st_codeVMer == 200, "Stauts code received is " + str(self.st_codeVMer)

                def test_checkstaus(self):
                    assert self.resstatus == "success"

                def test_checkApprove(self):
                    assert self.checkApprove == "APPROVED", "Expected approved but got " + self.checkApprove

                def getmer(self):
                    if self.resstatus == "success" and self.checkApprove == "APPROVED":
                        self.getmer = "Yes"
                        return self.getmer

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
                def getmer(self):
                    self.getmer = "No"
                    return self.getmer

        verifyCheck()

    getmer = "Yes"


else:
    getmer = "No"








