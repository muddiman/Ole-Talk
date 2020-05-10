"""UNIT TESTS for 'standard_response_lib.py' module. \n 
"""

# from standard_response_lib import std_response
import unittest
import json

std = __import__("src.libs.standard_response_lib.py")

def setUp():
    pass

class Test_standard_response_lib(unittest.TestCase):
    def test_std_response(self):
        status_code = 400
        response_msg = "Error: Exception thrown"
        expected = {
            'statusCode':status_code,
            'body': json.dumps({
                'userid': 'SERVER MESSAGE',
                'text': f"****** ATTN: {response_msg}. ******"
            })
        }
        result = std_response(status_code, response_msg)        
        self.assertEqual(result, expected)


"""         jsonObj = json.dumps({
            "userid": "SERVER MESSAGE",
            "text": "****** Success!!. ******"
        }) """

"""     def test_lambda_handler(self):
        pass

    def test_connectToChat(self):
        pass

    def test_checkConnection(self):
        pass
 """


if __name__ == "__main__":
    unittest.main()
