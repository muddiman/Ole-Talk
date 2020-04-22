"""LAMBDA EXECUTION MODULE FOR AWS LAMBDA FUNCTIONS.    \n
Executes Lambda Functions (lambda_handler) locally.
LAMBDA APPLICATION:
lAMBDA FUNCTION:    ANY

"""


import os
import json
import Lambda_ConnectToChat 
import Lambda_broadcastMsg
import Lambda_ChatServer
import Lambda_DisconnectFromChat 



CONTEXT=None

WD=os.getcwd()
PATH=os.path.join(WD, 'Ole-Talk', 'src', 'json', 'db_data_stream.json')
# FILE_PATH=os.path.join(WD, 'Ole-Talk', 'src', 'json', 'disconnection_request.json')
COMPLETE_FILE_PATH=os.path.join(WD, 'Ole-Talk', 'src', 'json', 'disconnection_request.json')


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

incoming_message = {
    'body': {
        'userid': 'guest',
        'text': 'An incoming message!'
    }
}

def file_handler(file_path):
    file = open(file_path, "rt")
    in_memory = file.read()
    file.close()
    return json.loads(in_memory)



#           ***MAIN***
connection_response = Lambda_ConnectToChat.lambda_handler(request_object, CONTEXT)
print(connection_response)
broadcast_msg_response = Lambda_broadcastMsg.lambda_handler(file_handler(PATH), CONTEXT)
print(broadcast_msg_response)
chat_serve = Lambda_ChatServer.lambda_handler(incoming_message, CONTEXT)
print(chat_serve)
disconnect_response = Lambda_DisconnectFromChat.lambda_handler(file_handler(COMPLETE_FILE_PATH), CONTEXT)
print(disconnect_response)
