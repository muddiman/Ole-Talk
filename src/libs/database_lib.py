"""
    Dynamodb access methods specifically for interacting with web socket connection
    tables and chat room tables.
"""

#   DATBASE LIBRARY

import json
import boto3
from botocore.exceptions import ClientError


#       ******DATABASE FUNCTIONS******      

#   Database functionality


class Dbase:
    # Class properties
    AWS_REGION='us-east-1'
    RESOURCE= boto3.resource(
                    'dynamodb',
                    region_name=AWS_REGION,
                    # aws_access_key_id='AKIA5B2GHECEBXFINYNY', 
                    # aws_secret_access_key='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'
                    )


    def __init__(self, table_name):  #, attr_name_list):
        self.table = Dbase.RESOURCE.Table(table_name)


    def insert_record(self, **kwargs):
        """Add an item to the database table.   \n
        :param list: attributes     \n 
        :return: str   \n
        """
        try:
            self.table.put_item(
                    Item=kwargs
                )
            return f"Record: {kwargs} was successfully entered into {self.table} table."
        except ClientError as err:
            return err.response['Error']['Message']


    def delete_record(self, partition_key, attribute):
        """Delete entry in Table.    \n 
        """
        try:
            self.table.delete_item(
                            Key={
                                partition_key: attribute
                            }
                        )
            return f"{partition_key}: {attribute} was deleted."
        except ClientError as err:
            return err.response['Error']['Message']


    def get_record(self, partition_key, attribute):
        try:
            response = self.table.get_item(
                Key={
                    partition_key: attribute
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
                    # aws_access_key_id='AKIA5B2GHECEBXFINYNY', 
                    # aws_secret_access_key='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'
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


#   =================================================================================================

# Test Code

if __name__ == "__main__":
    test = Dbase('test_table')
    print(f"Table Name: {test.table}")
    # print(f"Attribute Names: {test.attribute_names}")
    print(test.insert_record(column1='good', column2='OK'))
    print(test.get_record('column1', 'good'))
    print(test.delete_record('column1','good'))
    

    connections = Dbase('ChatSvrConnections')
    print(f"Table Name: {connections.table}")
    # print(f"Attribute Names: {connections.attribute_names}")
    print(connections.insert_record(connectionId='wwdsa123', roomId='chat123'))
    print(connections.get_record('connectionId', 'wwdsa123'))
    print(connections.delete_record('connectionId', 'wwdsa123'))

    # test_table = DynamoTable('test_table')
    # test_table.create_table('column1')


