"""Lambda Application:  Chat Server
@Project CodeName:  'Kaity'
@Application:       'OLE TALK'
@Module:            'connectToChat'
"""

import json
import boto3
from libs import database_lib as dlib
from libs import standard_response_lib as std_lib
from botocore.exceptions import ClientError



CHAT_SVR=dlib.Dbase('ChatSvrConnections')


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
    Item={
        'connectionId': connect_id,
        'userid': user_id
    }
    code, msg = CHAT_SVR.insert_record(**Item)   
    return std_lib.std_response(code, msg)

def checkConnection():
    pass




# Copyright (c) 2020 Gallatin Engineering Ltd. All Rights Reserved.