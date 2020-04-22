"""Lambda Application:  Chat Server     \n
@Project CodeName:  'Kaity'             \n
@Application:       'OLE TALK'          \n
@Module:            'connectToServer'   \n
"""


import json
import standard_response_lib as std_lib



def  lambda_handler(event, context): 
    if event['requestContext']['connectionId'] != None:
        return std_lib.std_response(200, '***Connected to server***')
    else:
        return std_lib.std_response(500, '***Could not connect to server!***')



# Copyright (c) 2020 Gallatin Engineering Ltd. All Rights Reserved.

