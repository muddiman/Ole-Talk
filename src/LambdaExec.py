"""LAMBDA EXECUTION MODULE FOR AWS LAMBDA FUNCTIONS.    \n
Executes Lambda Functions (lambda_handler) locally.
LAMBDA APPLICATION:
lAMBDA FUNCTION:    ANY

"""


import json
import Lambda_ConnectToChat 
import lambda_broadcastMsg


CONTEXT=None
PATH=r"C:\Users\roger\Documents\Personal\dev\AllFours\All_Fours_Chat_Server\src\json\db_data_stream.json"

request_object = {
    'requestContext': {
        'connectionId': 'example_id'
    },
    'body': json.dumps({
                'route': 'route_id',
                'userid': 'sample_user',
                'text': 'sample_text_msg'
            })
}

f = open(PATH, "rt")
record_file = f.read()
request_records = json.load(f)



def build_request_obj():
    pass


#   MAIN
connect = Lambda_ConnectToChat.lambda_handler(request_object, CONTEXT)
print(connect)
broadcast = lambda_broadcastMsg.lambda_handler(request_records, CONTEXT)
f.close()
print(broadcast)
