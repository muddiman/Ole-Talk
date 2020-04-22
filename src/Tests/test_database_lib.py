"""TESTS file for 'database_lib.py' module. \n 
"""
import unittest
from database_lib import Dbase


class Test_Dbase(unittest.TestCase):
    def test_insert_record(self):
        # self.assertEqual()
        pass    

    def test_get_record(self):
        # self.assertEqual()
        pass

    def test_delete_record(self):
        # self.assertEqual()
        pass


class Test_DynamoTable(unittest.TestCase):
    def test_create_table(self):
        # self.assertEqual()
        pass

    def test_delete_table(self):
        # self.assertEqual()
        pass


if __name__ == '__main__':
    unittest.main()