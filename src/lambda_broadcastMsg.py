"""THIS FUNCTION IS TRIGGERED by dynamodb streams. whenever a new entry in the chat table is detected,
the event passes through this function and send the message to all connected websockets.
@Project CodeName:  'Kaity'
@Application:       'OLE TALK'
@Module:            'broadcastMsg'
"""


import json
import requests
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


# CONSTANTS
DB=boto3.resource("dynamodb")
STD_ERR={
    "statusCode":400,
    "body":json.dumps({
        "userid": "SYSTEM MESSAGE",
        "text": f"   ****** ATTN: lAMBDA ERROR: could not execute function. ******"
    })
}
STD_SUCCESS_MSG={
    'statusCode':200,
    'body': json.dumps({
        'userid': 'SERVER MESSAGE',
        'text': f"   ****** ATTN: Message sent to all connections. ******"
    })
}

# Main 
def lambda_handler(event, context):
    """
    :param (list): event -- list of db records      \n
    :returns: (dict) status msg
    """
    try:
        # process incoming db stream and send msg in db records to all connection ids
        db_stream_handler(event)
        print(STD_SUCCESS_MSG)
        return STD_SUCCESS_MSG
    except:
        print(STD_ERR)
        return STD_ERR


# Support Functions
def db_stream_handler(stream):
    """Sends a post request with details from DBstream to ALL connection ids in list of connection ids.   \n
    :param (str): stream -- lambda event: db stream     \n
    :returns: success or error dict      \n
    """
    # stream: list of db Records
    for record in stream['Records']:
        if record['eventName'] == 'INSERT':
            user = record['dynamodb']['NewImage']['user']['S']
            try:
                response = DB.Table('ChatSvrConnections').scan(
                    FilterExpression=Attr('userid').eq(user)
                )
            except:
                return {
                        "statusCode":400,
                        "body":json.dumps({
                            "userid": "SYSTEM MESSAGE",
                            "text": f"   ****** ATTN: DATABASE ERROR: Dynamodb scan request rejected. ******"
                        })
                    }                
            payload = json.dumps({
                        "body":{
                            'text': record['dynamodb']['NewImage']['text']['S'],
                            'userid': record['dynamodb']['NewImage']['user']['S'],
                            'timestamp': record['dynamodb']['NewImage']['timestamp']['S']
                            }
                        })            
            for item in response['Items']:
                connection_ID = item['connectionId']
                if send_msg(connection_ID, payload) == False:
                    return {
                            "statusCode":400,
                            "body":json.dumps({
                                "userid": "SYSTEM MESSAGE",
                                "text": f"   ****** ATTN: HTTP REQUEST ERROR: post request failed. ******"
                            })
                        }


def send_msg(id, payload):
    """     \n
    :param (str): payload -- chat message object in json format.  \n
    :param (str): id -- websocket client connection id.       \n
    :returns: boolean (successful/unsuccessful)
    """
    url=f'https://ljy888l5y0.execute-api.us-east-1.amazonaws.com/dev/@connections/{id}'
    try:
        requests.post(url, json=payload)
        return True
    except Exception as err:
        print(err)
        return False
            


#     ******  Copyright (c) 2020 - Gallatin Engineering. All rights reserved. ******