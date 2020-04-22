"""THIS FUNCTION IS TRIGGERED by dynamodb streams. whenever a new entry in the chat table is detected,
the event passes through this function and send the message to all connected websockets.
@Project CodeName:  'Kaity'
@Application:       'OLE TALK'
@Module:            'broadcastMsg'
@Web:               'https://gallatinengineering.com/pages/chat.html
@Contact:           'developers@gallatinengineering.com'
:copyright: (c) 2020 Gallatin Enginering Ltd. All Rights Reserved.
"""


import json
import requests
import boto3
from libs import standard_response_lib as std_lib
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


# CONSTANTS
DB=boto3.resource("dynamodb")


# Main 
def lambda_handler(event, context):
    """Send incoming db streams to all web socket connection.   \n
    :param (list): event -- list of db records      \n
    :returns: (dict) status msg
    """
    return db_stream_handler(event)


# Support Functions
def db_stream_handler(stream):
    """Sends a post request with details from DBstream to ALL connection ids in list of connection ids.   \n
    :param (str): stream -- lambda event: db stream     \n
    :returns: success or error dict      \n
    """
    # stream: list of db Records
    for record in stream['Records']:
        if record['eventName'] == 'INSERT':
            user = record['dynamodb']['NewImage']['Username']['S']
            try:
                # extract connectionId from 'ChatSvrConnections' table that matches with 'user'
                response = DB.Table('ChatSvrConnections').scan(
                    FilterExpression=Attr('userid').eq(user)
                )
            except:
                return std_lib.std_response(400, " DATABASE ERROR: Dynamodb scan request rejected.")

            # construct payload               
            payload = json.dumps({
                        "body":{
                            'text': record['dynamodb']['NewImage']['Message']['S'],
                            'userid': record['dynamodb']['NewImage']['Username']['S'],
                            'timestamp': record['dynamodb']['NewImage']['Timestamp']['S']
                            }
                        })            
            for item in response['Items']:
                connection_ID = item['connectionId']
                if send_msg(connection_ID, payload) == False:
                    return std_lib.std_response(400, "HTTP REQUEST ERROR: request rejected.")

            return std_lib.std_response(200, "HTTP REQUEST: Accepted!")



def send_msg(id, payload):
    """Sends payload (in json format) as a post request to the websocket api, and the api
    then forwards the payload to the connected websocket client.     \n
    :param (str): payload -- chat message object in json format.  \n
    :param (str): id -- websocket client connection id.       \n
    :returns: (boolean) successful/unsuccessful
    """
    url=f'https://ljy888l5y0.execute-api.us-east-1.amazonaws.com/dev/@connections/{id}'
    try:
        x = requests.post(url, json=payload)
        print(x)
        return True
    except Exception as err:
        print(err)
        return False
            

# def std_response(status_code, response_msg):
#     return {
#     'statusCode':status_code,
#     'body': json.dumps({
#         'userid': 'SERVER MESSAGE',
#         'text': f"   ****** ATTN: {response_msg}. ******"
#     })
# }



#     ******  Copyright (c) 2020 - Gallatin Engineering. All rights reserved. ******