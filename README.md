# IPN_API_Testing_Automation
About the structure of project:
Inputs:
  1. Login credentials to be provided by user in authLogin.json.
  2. Creating Merchant Data to be provided by user in createMer.json
  3. Request ID will be generated and written in verifyMer.json automatically.
  4. Updating Merchant Data to be provided by user in updateMer.json where merchant id will be autoupdated if complete process 
       is run. However if only update Merchant is to be run, even merchant id must be specified by user.
  5. Same goes for delete merchant input. If process is automatic, merchant id will be updated but if only delete is to be run then merchant id must by provided by the user inside test_6DeleteMerchant.py.

     How to run?
     1. If entire process is to be run:  pytest -s -v (Give the inputs as mentioned above.)
     2. If each process is to be run separately: pytest location\test.py -s -v
    
        Note: Running all the process creates, updates and deletes and shows if all the test cases were successful or not.In order to check each response, please run the files separately.
