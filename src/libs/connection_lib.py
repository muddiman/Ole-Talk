
import json
from time import ctime
from chat_lib.database_lib import Dbase, DynamoTable


class Web_Socket(object):
    def __init__(self, connection_id):
        self.connection_id = connection_id


    def connect(self, chat_room):
        connection_table = Dbase('ChatSvrConnections')
        connection_table.insert_record(connectionId=self.connection_id, roomId=chat_room)


    def disconnect(self):
        connection_table = Dbase('ChatSvrConnections')
        connection_table.delete_record('connectionId', self.connection_id)



class Chat_Room(object):
    def __init__(self, room_id):
        self.room_id = room_id


    def create(self, connection_id):
        """Creates a chat room: \n 
        \t \t creates a new database table representing the chat rooom.     \n  
        """
        connection_db = Dbase('ChatSvrConnections')
        connection = connection_db.get_record('connectionId', connection_id)
        room_id = connection['roomId']
        chat_table = DynamoTable(room_id)
        return chat_table.create_table('timestamp')


    def close(self):
        pass

    def isExisting(self):
        chat_table = Dbase(self.room_id)
        # get table
        if True:
            return True
        else:
            return False

    # def join(self):
    #     chat_db = Dbase(self.room_id)
    #     chat_db.insert_record({
    #                     ''
    #     })


    def leave(self):
        pass

    def list_members(self):
        """Scans connection database table for connections with the same, specified room id, \n  
        :return: list --> connectionIds
        """
        # TODO: Implement 'scan' dynamodb command
        pass


    def broadcast_message(self, timestamp):
        chat_table = Dbase(self.room_id)
        msg_record = chat_table.get_record('timestamp', timestamp)
        msg = json.dumps({ 
                    'msg' : msg_record['msg'],
                    'user': msg_record['user'],
                    'time': msg_record['timestamp']
                })
        # TODO: send msg to each connection in chat room



class Message():
    def __init__(self, incoming=None, outgoing=None):
        if incoming:
            self.extract(incoming)
        if outgoing:
            # self.read(chat_room, timestamp)
            

    def package(self):
        return json.dumps({
            'timestamp': ctime,
            'user': self.handle,
            'msg': self.msg
        })

    def extract(self, json_msg):
        msg_obj = json.loads(json_msg)
        self.timestamp = ctime
        self.handle = msg_obj['user']
        self.msg = msg_obj['text']

    def broadcast(self):
        pass

    def save(self):
        pass

    def read(self, chat_room, timestamp):
        chat_db = Dbase()
