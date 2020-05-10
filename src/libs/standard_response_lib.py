"""Server Response Template Module.    \n
ALL SERVER RESPONSES will follow this template, such that
it can be ignored by the client but can be accessed for 
debugging purposes. Combined with a logging module; this 
could considerably speed up debugging tasks.    \n
Delivers a dict with a json object body, for a given status code and accompanying message.  \n
"""



import json


def std_response(status_code, response_msg):
    """Formats server messages in a standardised framwork
    using the template below.   \n
    :param (int): status_code - standardized HTTP response code associated
    with these errors and exceptions.  \n
    :param (str): response_msg - short text highlighting the problem or status.   \n
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
