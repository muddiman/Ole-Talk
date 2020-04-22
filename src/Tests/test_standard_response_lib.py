"""UNIT TESTS for 'standard_response_lib.py' module. \n 
"""


from ..libs import standard_response_lib 
import unittest
import json


def setUp():
    pass

class Test_standard_response_lib(unittest.TestCase):
    def test_std_response(self):
        code = 200
        msg = "Success!!"
        jsonObj = json.dumps({
            "userid": "SERVER MESSAGE",
            "text": "****** Success!!. ******"
        })
        expected = {
            "statusCode": 200,
            "body": jsonObj
            }
        result = libs.standard_response_lib.std_response(code, msg)        
        self.assertEqual(result, expected)




"""     def test_lambda_handler(self):
        pass

    def test_connectToChat(self):
        pass

    def test_checkConnection(self):
        pass
 """


if __name__ == "__main__":
    unittest.main()
