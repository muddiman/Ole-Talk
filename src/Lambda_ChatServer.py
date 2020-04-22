"""Main Lambda Function for chat server's incoming messages. Stores incoming messages in the chat database.    \n 
TODO:   implement chat room option.     \n
        separate db code from main code and put connection code in a separate boolean function.    \n 
"""

import boto3
import json
from time import ctime
from libs import database_lib as dlib
from libs import standard_response_lib as std_lib
from botocore.exceptions import ClientError


# CONSTANTS
CHAT_ROOM='help-desk'
# AWS_REGION="us-east-1"
# DB_RESOURCE = boto3.resource(
#                     'dynamodb', 
#                     region_name=AWS_REGION
#                     )
# MSG_TABLE = DB_RESOURCE.Table(CHAT_ROOM)


def lambda_handler(event, context):
    """Make db entry in the Connections table and the return a system success/failure message.    \n 
    :param dict: event  \n
    :param dict: context    \n 
    :returns: dict - status response    \n 
    """
    # parse event, ignore (aws) lambda context
    # event_body = json.load(event['body'])
    event_body = event['body']
    userid = event_body['userid']
    text = event_body['text']
    
    # store msg in chat table
    msg_dict = build_chat_msg(userid, text)
    statusCode, statusMsg = store_chat_msg(msg_dict)
    return std_lib.std_response(statusCode, statusMsg)
  

def build_chat_msg(userid_, msg_text):
    return {
        "timestamp": ctime(),
        "userid": userid_,
        "msg_text": msg_text
    }


def store_chat_msg(item):
    chat_db = dlib.Dbase(CHAT_ROOM)
    code, msg = chat_db.insert_record(**item)  
    # print(msg)
    return code, msg


#   Copyright (c) 2020. Gallatin Engineering Ltd. All Rights Reserved.