"""Lambda Application:  Chat Server
@Project CodeName:  'Kaity'
@Application:       'OLE TALK'
@Module:            'connectToChat'
"""

import json
import json
import boto3
from botocore.exceptions import ClientError


AWS_REGION="us-east-1"
DB_RESOURCE = boto3.resource(
                    'dynamodb', 
                    region_name=AWS_REGION
                    )
CONNECTIONS = DB_RESOURCE.Table('ChatSvrConnections')


def lambda_handler(event, context):
    """Lambda function - connectToChat.     \n
    :param (dict): event --> API (integration) Request    \n
    :param (obj): context --> API request's context object (the context of the 'triggering' event)\n
    :returns: response (obj)    \n
    """
    id = event['requestContext']['connectionId']
    userid = json.loads(event['body'])['userid']
    # userid = event['body']['userid']    # change back to json after tests
    return connectToChat(id, userid)




def connectToChat(connect_id, user_id):
    """Simulates connecting to a chat server, by entering 
    a user's name and id into the 'ChatSvrConnect' database table.  \n 
    :param (str): connect_id -- the websocket id given by the API.  \n
    :param (str): user_id -- the username chosen by the user.   \n 
    :return: (dict) 'system response' -- includes status code & message.  \n
    """
    try:
        CONNECTIONS.put_item(
                    Item={
                        'connectionId': connect_id,
                        'userid': user_id
                    }
                )
        # system response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'userid': 'SERVER MESSAGE',
                'text': f"   ****** ATTN: {id} connected to chat server. ******"
            })
        }
    except ClientError as err:
        # system response
        return {
            'statusCode': 400,
            'body': json.dumps({
                'userid': 'SERVER MESSAGE',
                'text': err.response['Error']['Message']
            })
        }
  
# Copyright (c) 2020 Gallatin Engineering Ltd. All Rights Reserved.