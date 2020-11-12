"""DYNAMODB MODULE      \n
@DISCRIPTION: Dynamodb access methods specifically for interacting with web socket connection
tables and chat room tables.    \n
@VERSION: 1.2.0
"""

#   DATABASE LIBRARY

import json
import boto3
from botocore.exceptions import ClientError


#       ******DATABASE FUNCTIONS******      



class Dbase:
    # Class properties
    AWS_REGION='us-east-1'
    RESOURCE= boto3.resource(
                    'dynamodb',
                    region_name=AWS_REGION,
                    )


    def __init__(self, table_name):  #, attr_name_list):
        self.table = Dbase.RESOURCE.Table(table_name)


    def insert_record(self, **kwargs):
        """Add an item to the database table.   \n
        :param (dict): attributes     \n 
        :return: (int) response code, (str) response msg  \n
        """
        try:
            self.table.put_item(
                    Item=kwargs
                )
            return 200, f"Record: {kwargs} was successfully entered into {self.table} table."
        except ClientError as err:
            return 500, err.response['Error']['Message']


    def delete_record(self, partition_key, key_attribute):
        """Delete entry in Table.    \n 
        """
        try:
            self.table.delete_item(
                            Key={
                                partition_key: key_attribute
                            }
                        )
            return 200, f"{partition_key}: {key_attribute} was deleted."
        except ClientError as err:
            return 500, err.response['Error']['Message']


    def get_record(self, partition_key, key_attribute):
        try:
            response = self.table.get_item(
                Key={
                    partition_key: key_attribute
                }
            )
            return response['Item']
        except ClientError as err:
            return err.response['Error']['Message']



class DynamoTable(object):
    # Class properties
    AWS_REGION='us-east-1'
    RESOURCE= boto3.resource(
                    'dynamodb',
                    region_name=AWS_REGION,
                    )


    def __init__(self, table_name):
        self.table_name = table_name


    def create_table(self, partition_key):
        key_schema = {
                        'AttributeName': partition_key,
                        'KeyType': 'HASH'
                    }
        attr_defns = {
                            'AttributeName': partition_key,
                            'AttributeType': 'S'
                    }
        try:
            new_table = DynamoTable.RESOURCE.create_table(
                                    TableName = self.table_name,
                                    KeySchema = [key_schema],
                                    AttributeDefinitions = [attr_defns],
                                    ProvisionedThroughput={
                                        'ReadCapacityUnits': 5,
                                        'WriteCapacityUnits': 5
                                    }
                                )
            new_table.meta.client.get_waiter('table_exists').wait(TableName=self.table_name)
            print(new_table.item_count)
            return f"New table {self.table_name} created."
        except ClientError as err:
            return err.response['Error']['Message']


    def delete_table(self):
        DynamoTable.RESOURCE.Table(self.table_name).delete()


#   =================================================================================================

# Test Code

if __name__ == "__main__":
    # test = Dbase('test_table')
    # print(f"Table Name: {test.table}")
    # print(f"Attribute Names: {test.attribute_names}")
    # print(test.insert_record(column1='good', column2='OK'))
    # print(test.get_record('column1', 'good'))
    # print(test.delete_record('column1','good'))
    
    """ 
    connections = Dbase('ChatSvrConnections')
    print(f"Table Name: {connections.table}")
    # print(f"Attribute Names: {connections.attribute_names}")
    print(connections.insert_record(connectionId='wwdsa123', roomId='chat123'))
    print(connections.get_record('connectionId', 'wwdsa123'))
    print(connections.delete_record('connectionId', 'wwdsa123'))
    """
    # test_table = DynamoTable('NEW_TABLE')
    # test_table.create_table('Room')
    # test_table.delete_table()




#               ******Copyright (c) 2019-2020. Gallatin Engineering Ltd. All Rights Reserved.******