"""Lambda Application:  Chat Server     \n
@Project CodeName:  'Kaity'             \n
@Application:       'OLE TALK'          \n
@Module:            'connectToServer'   \n
@AUTHOR/PROGRAMMER: muddicode/sauceCode
@VERSION: 1.0.0
"""


import json
import libs.standard_response_lib #as std_lib
import libs.database_lib


def  lambda_handler(event, context): 
    if event['requestContext']['connectionId'] != None:
        response = openConnection(event['requestContext']['connectionId'])
        if response["statusCode"] == 200:
            return libs.standard_response_lib.std_response(200, '***Connected to server***')
        else:
            return response
    else:
        return libs.standard_response_lib.std_response(500, '***Could not connect to server!***')


def openConnection(id_, userid):
    """Connects to Chat Server. Inserts an entry of the specified connection id in the connections
    table of the database.   \n
    :param (string): connection id  \n
    :param (string): userid -- username or chat user handle
    :return: (string) success/fail msg  \n
    """
    connections = new libs.database_lib.Dbase("connections")
    statusCode, msg = connections.insert(connectionId=id_, userid=userid)
    if statusCode == 200:
        return libs.standard_response_lib.std_response(200, '***connection id successfully inserted into database***')
    else:
        return libs.standard_response_lib.std_response(400, '***database insertion failed***')


def checkConnection(id_):
    """Checks connection table in database for an entry identical to the specified connection id.   \n
    :param (string): id_ connection id  \n
    :return: (boolean) True/False   \n
    """
    connections = libs.database_lib.Dbase("connections")
    response = connections.get_record(connectionId=id_)
    if response['connectionId'] == id_:
        return True
    else:
        return False





# Copyright (c) 2020 Gallatin Engineering Ltd. All Rights Reserved.

