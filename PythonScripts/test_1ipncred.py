import json
import requests




#-------------------------- RUN USING pytest or python -m pytest in terminal -------------------#

url = "https://ipn-tms-staging.qrsoundboxnepal.com/api/v1/auth/login/"
location = "C:\\Users\\sandesh.kafle\\Documents\\UiPath\\Bitskraft_IPN\\Input\\"
with open(location +'authLogin.json','r') as ipfile:
    json_input = ipfile.read()

request_json = json.loads(json_input)
print(request_json)
res = requests.post(url, request_json)
st_code_login = res.status_code

# class Status:
#     def __init__(self,response, stcode):
#         self.response = response
#         self.stcode = stcode
#
#     def get_stcode(self):
#         return self.stcode
#     def get_response(self):
#         return self.response


def test_status_code():
    #checkStatus = Status(res, st_code_login)
    #stcode = checkStatus.get_stcode()
    assert st_code_login == 200, "Status code received is " + str(st_code_login)

if st_code_login == 200:
    cookies = res.cookies
    json_response_login = res.json()

    access_token = json_response_login["access"]
    createMerchant = "Yes"

    def test_access_token():
        assert len(access_token) != 0, "Access token was not generated."

    def test_isObject():
        assert json_response_login["user"] != None, "User does not exists."

    if len(access_token) == 0 or json_response_login["user"] == None :
        createMerchant = "No"
else:
    createMerchant = "No"

print("Test1 done")












