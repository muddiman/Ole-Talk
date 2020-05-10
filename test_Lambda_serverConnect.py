"""UNITTESTS for 'Lambda_ConnectToChat.py' module. \n 
"""


from src.libs.standard_response_lib import std_response
from src.Lambda_serverConnect import lambda_handler, openConnection, checkConnection
import unittest

# svr = __import__("src.Lambda_serverConnect.py")
# lambda_handler = svr.lambda_handler
# openConnection = svr.openConnection

event = {
    "requestContext": {
        "connectionId": None
    }
}
context = None

def setUp():
    """Insert daffy_duck into connection table of database.     \n
    """
    pass

def tearDown():
    """Remove daffy_duck from connection table of database.     \n
    """
    pass


class Test_serverConnect(unittest.TestCase):

    def test_lambda_handler(self):
        expected = std_response(500, '***Could not connect to server!***')
        actual = lambda_handler(event, context)
        self.assertEqual(actual, expected)

    def test_openConnection(self):
        actual = openConnection("rac200")
        event = {
            "requestContext": {
                "connectionId": "rac200"
            }
        }
        expected = True
        self.assertEqual(actual, expected)

    def test_checkConnection(self):
        """"""
        id_ = "daffy_duck"
        actual = checkConnection(id_)
        expected = True
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
