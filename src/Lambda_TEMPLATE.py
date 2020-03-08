"""Lambda Application:  Chat Server

@Project CodeName:  'Kaity'
@Application:       'OLE TALK'
@Module:            'MODULE TEMPLATE'
"""


import json

STD_ERR={
    "statusCode":400,
    "body":json.dumps({
        "userid": "SYSTEM MESSAGE",
        "text": f"   ****** ATTN: lAMBDA ERROR: could not execute function. ******"
    })
}

def lambda_handler(event, context):
    """Lambda function - connectToChat.     \n
    :param (dict): event --> API (integration) request    \n
    :param (obj): context --> API request's context object (the context of the 'triggering' event)\n
    :returns: response (obj)    \n
    """
    id = event['requestContext']
    userid = json.loads(event['body'])['userid']
    # userid = event['body']['userid']    # change back to json after tests
    
    return special_function(params)


def special_function(*args, **kwargs):
    """ function description
    :param (list): args
    :param (dict): kwargs
    :returns: dict 
    """
    #               ***code***
    try:
        # access a database function
        # system response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'userid': 'SERVER MESSAGE',
                'text': f"   ****** ATTN: {id} connected to chat server. ******"
            })
        }
    except as err:
        # system response
        return {
            'statusCode': 400,
            'body': json.dumps({
                'userid': 'SERVER MESSAGE',
                'text': err.response['Error']['Message']
            })
        }


def support_function(*args, **kwargs):
    """
    :param (list): args
    :param (dict): kwargs
    :return:
    """
    pass

# Copyright (c) 2020 Gallatin Engineering Ltd. All Rights Reserved.

