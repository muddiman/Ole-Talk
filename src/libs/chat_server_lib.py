

#   BROADCAST MSG

import json
import boto3
from time import ctime
from botocore.Exceptions import ClientError
from chat_lib.database_lib import Dbase, DynamoTable
from chat_lib.connection_lib import Web_socket, Chat_Room


class Chat_Server():
    """Interface between web socket api and chat database.  \n 
    """
    #   Class Properties
    all_rooms = []
    all_connections = []
    MAX_CHAT_ROOMS=4
    MAX_CONNECTIONS_PER_ROOM=4
    CONNECTION_TABLE='ChatSvrConnections'
    CONNECTIONS_DB = Dbase(CONNECTION_TABLE)

    # Instance methods & properties
    def __init__(self, connection_id, chat_room_id):
        """connections & rooms
        """
        # existing connections
        Chat_Server.all_connections = self.get_existing_chat_connecions()
        # existing rooms
        Chat_Server.all_rooms = self.get_existing_chat_rooms()
        # new connection
        self.connection_id = connection_id
        if self.connection_id not in Chat_Server.all_connections:
            Chat_Server.all_connections = self.connection_id
        # new room
        self.room_id = chat_room_id
        if self.room_id not in Chat_Server.all_rooms
            Chat_Server.all_rooms = self.room_id
        # process connection
        self.connection = Web_Socket(self.connection_id)

        # self.connection_details = {'id': connection_id, 'chatroom': chat_room_id}
        # if the chat room message table doesnt exist, create new chat room (ie: a chat room message table)
        if chat_room_id not in Chat_Server.all_rooms:
            Chat_Server.rooms[len(Chat_Server.rooms)] = chat_room_id

    
    def get_existing_chat_connecions(self):
        pass


    def get_existing_chat_rooms(self):
        pass


    def connection_handler(self):
        """Accepts incoming connections and stores them in connections table in chat server databaase.  \n 
        """
        # connect to server
        self.connection.connect(self.room_id)
        # Chat_Server.CONNECTIONS_DB.insert_record(connection_id=self.connection['id'], room_id=self.connection['chat_room'])
        chat_room = Chat_Room(self.room_id)
        if chat_room.isExisting() is False:
            chat_room.create(self.room_id)
        # join chat room
        chat_room.join()
        # TODO: reject connection
        pass


    def message_handler(self, ):
        """Accepts incomming messages and stores them in chat_room table of chat database. \n 
        """
        # place msg in chat room 
        pass

    
    # optional
    def broadcast_message(self):
        """Takes new entries from the chat room table of the chat database 
        and sends them to each web socket connection in the database with same room id.
        """
        pass

    def disconnection_handler(self):
        """Accepts a disconnection message from the API and remover
        entry in ChatSvrConnections table.  \n 
        """
        self.connection.disconnect()

    # chat = Chat_Server()