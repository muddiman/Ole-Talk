"""Server Response Template.    \n
Delivers a dict with a json object body, for a given status code and accompanying message.  \n
"""



import json


def std_response(status_code, response_msg):
    """
    :param (int): status_code - HTTP response code  \n
    :param (str): response_msg - text   \n
    :returns: (dict) formatted dict with a json object in the  'body', containing the userid (SYSTEM MESSAGE)
    and text message.       \n
    """
    return {
    'statusCode':status_code,
    'body': json.dumps({
        'userid': 'SERVER MESSAGE',
        'text': f"****** ATTN: {response_msg}. ******"
    })
}
