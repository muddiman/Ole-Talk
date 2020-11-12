"""DYNAMODB MODULE:      \n
Dynamodb access methods specifically for interacting with web socket connection
tables and chat room tables.    \n
    @AUTHOR/PROGRAMMER: muddicode/sauceCode \n
    @VERSION: 1.0.0 \n
"""

#   DATABASE LIBRARY

import json
import boto3
from botocore.exceptions import ClientError


#   CONSTANTS
DB_TABLE='CHAT_DB'      #   Will always be CHAT_DB


#       ******DATABASE FUNCTIONS******      



class Dbase:
    # Class properties
    AWS_REGION='us-east-1'
    RESOURCE=boto3.resource(
                    'dynamodb',
                    region_name=AWS_REGION,
                    )
    CLIENT=boto3.client('dynamodb')


    def __init__(self, table_name=DB_TABLE):  #, attr_name_list):
        self.table = Dbase.RESOURCE.Table(table_name)
        self.client = Dbase.CLIENT


    def insert_record(self, **kwargs):
        """Add an item to the database table.   \n
        :param (dict): kwargs - key-value pairs of item attributes     \n 
        :return: (int) response code, (str) response msg  \n
        """
        try:
            self.table.put_item(
                    Item=kwargs
                )
            return 200, f"Record: {kwargs} was successfully entered into {self.table} database table."
        except ClientError as err:
            return 500, err.response['Error']['Message']


    def delete_record(self, key_attribute, partition_key='id' ):
        """Delete entry in Table.    \n 
        :params string: key_attribute - the item id  \n
        :params string: partition_key='id'  \n
        :return: (int) statusCode - http status code, (string) message - status message \n
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


    def get_record(self, key_attribute, partition_key='id'):
        """Retrieves an entry from the database Table.    \n 
        :params string: key_attribute - the item id  \n
        :params string: partition_key='id'  \n
        :return: (int) statusCode - http status code, (string) message - status message \n
        """        
        try:
            response = self.table.get_item(
                Key={
                    partition_key: key_attribute
                }
            )
            return response['Item']
        except ClientError as err:
            return err.response['Error']['Message']


    def update_record(self, key_attribute, update_key, update_value, partition_key='id'):
        """Modifies an entry in the database Table.    \n 
        :params string: key_attribute - the item id  \n
        :params string: update_key - key to be modified   \n
        :params string: update_value - value to replace existing value  \n
        :params string: partition_key='id'  \n
        :return: (int) statusCode - http status code, (string) message - status message \n
        """
        self.table.update_item(
            Key={
                partition_key: key_attribute
            },
            UpdateExpression='SET update_key = :val1',
            ExpressionAttributeValues={
                ':val1': update_value 
            }
        )


    def scan_table(self):
        """Gets all records in the table.       \n
        :return: (dict) key - value output of the table.    \n
        """
        response = self.client.scan(
            TableName='ChatSvrConnections',
            Limit=123,
            Select='ALL_ATTRIBUTES'
        )
        return response


#   =================================================================================================

# Test Code

if __name__ == "__main__":
    test = Dbase()
    print(f"Table Name: {test.table}")
    print(test.insert_record(id='good', server='OK'))
    print(test.get_record('good'))
    print(test.delete_record('good'))
    

    connections = Dbase('ChatSvrConnections')
    print(f"Table Name: {connections.table}")
    print(connections.insert_record(connectionId='wwdsa123', roomId='chat123'))
    print(connections.get_record('wwdsa123', 'connectionId'))
    print(connections.update_record('wwdsa123', 'roomId', 'new room', partition_key='connectionId'))
    print(connections.delete_record('wwdsa123', 'connectionId'))
    print(connections.scan_table())


#   garbage code

"""
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
        # print(attr_defns)
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

"""
