import json
import boto3
from time import ctime
from libs import standard_response_lib as std_lib
from libs import database_lib as dlib
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


AWS_REGION='us-east-1'
DB=boto3.resource(
            'dynamodb',
            region_name=AWS_REGION
        )
  

def lambda_handler(event, context):
    # TODO implement
    conn_id = event['requestContext']['connectionId']
    # room = get_room_id(conn_id)
    # user_id = json.loads(event['body'])['userid']
    # close connection (delete db entry) 
    statusCode, statusMsg = disconnect_from_server(conn_id)
    return std_lib.std_response(statusCode, statusMsg)
    # {
    #     'statusCode': statusCode,
    #     'body': json.dumps({
    #         'userid' :  'SYSTEM MESSAGE',
    #         'text'   : f'  ****** ATTN: {statusMsg} ******    '
    #     })
    # }
    # broadcast user left the room
    # broadcastMsg(conn_id, statusMsg)
    # if no users connected to room, delete chat room(table)
    # response = DB.Table('ChatSvrConnections').scan(
    #     FilterExpression=Attr('roomId').eq(room)
    # )
    # items = response['Items']
    # print(items)
    # if len(items) == 0:
    #     # close chat room, ie. delete chat room message table
    #     DB.Table(room).delete()
        
        
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({
    #         "message": f"User: {user_id} has left the chat room."
    #     })
    # }


# def get_room_id(id):
#     try:
#         response = DB.Table('ChatSvrConnections').get_item(
#                             Key={
#                                 'connectionId': id
#                             }
#                         )
#         print(response['Item']['roomId'])
#         return response['Item']['roomId']
#     except ClientError as e:
#         return e.response['Error']['Message']


def disconnect_from_server(connectId):
    # delete entry in Connections Table
    # try:
    chat_db = dlib.Dbase('ChatSvrConnections')
    return chat_db.delete_record('connectionId', connectId)
        # DB.Table('ChatSvrConnections').delete_item(
        #                 Key={
        #                     'connectionId': connnectionId
        #                 }
        #             )
    #     return 200, f"User has left the chat room."
    # except ClientError as e:
    #     return 500, e.response['Error']['Message']
        
        
def broadcastMsg(userid, msg):
    Item={
        "timestamp": ctime(),
        "user": userid,
        "text": msg
    }    
    chat_db = dlib.Dbase('ChatSvrConnections')
    return chat_db.insert_record(**Item)
    # try:    
    #     DB.Table('help-desk').put_item(
    #             Item={
    #                 "timestamp": ctime(),
    #                 "user": user,
    #                 "text": msg
    #             }
    #         )
    # except ClientError as e:
    #     return e.response['Error']['Message']