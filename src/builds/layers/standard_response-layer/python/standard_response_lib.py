"""Server Response Template.    \n
@DISCRIPTION:   Delivers a dict with a json object body, for a given status code and accompanying message.  \n
@VERSION: 1.2.0
"""


import time
import json


def std_response(status_code, response_msg, server='chat.twomanallfours.com', chatroom='#default'):
    """
    :param (int): status_code - HTTP response code  \n
    :param (str): response_msg - text   \n
    :param (str): server - name of chat  server, relative to the requesting web app/site.   \n
    :param (str): chatroom - name of room where the message table will be stored  in the database.  \n
    :returns: (dict) formatted dict with a json object in the  'body', containing the userid (SYSTEM MESSAGE)
    and text message.       \n
    """
    return {
    'statusCode':status_code,
    'body': json.dumps({
        'timestamp': time.ctime(),
        'server': server,
        'room': chatroom,
        'userid': 'SERVER MESSAGE',
        'text': f"   ****** ATTN: {response_msg}. ******"
    })
}



#               ******Copyright (c) 2019-2020. Gallatin Engineering Ltd. All Rights Reserved.******