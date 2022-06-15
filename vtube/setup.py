import json
import os
from vtube.params import CUSTOM_PARAMS

import vtube.utils

CONFIG_FILE = 'config.json'

async def init(websocket):
    if os.path.exists(CONFIG_FILE):
        # Load token
        print('Loading token...')
        with open(CONFIG_FILE, "r") as config_file:
            data = json.load(config_file)
            authtoken = (data['authenticationkey'])
            # Authorization with token
            confirm = await vtube.utils.register_plugin(websocket, authtoken)
            if authtoken == "" or confirm["data"]["authenticated"] == False:
                # Invalid token; request for a new one
                print('Error Token Invalid')
                print('Fetching New Tokens...')
                authtoken = await vtube.utils.request_token(websocket)
                print(authtoken)
                print('Saving token...')
                data["authenticationkey"] = authtoken
                config_file.close()
                config_file = open(CONFIG_FILE, "w")
                config_file.write(json.dumps(data))
                config_file.close()
                print("Saving finished")
            else:
                # Authorization succeed
                config_file.close()
    else:
        # request for a token
        print('Fetching New Tokens...')
        authtoken = await vtube.utils.request_token(websocket)
        print(authtoken)
        # save token
        print('Saving token...')
        with open(CONFIG_FILE, "w") as config_file:
            config = {
                "authenticationkey": authtoken,
            }
            config_file.write(json.dumps(config))
            config_file.close()
        # Authorization with token
        await vtube.utils.register_plugin(websocket, authtoken)

    # fetch parameter list
    print("Fetching Parameters...")
    params_res = await vtube.utils.list_parameters(websocket)
    custom_params = set()
    for param_item in params_res['data']['customParameters']:
        custom_params.add(param_item['name'])

    # add missing params
    print("Registering Parameters...")
    for custom_param_name in CUSTOM_PARAMS:
        if custom_param_name not in custom_params:
            await vtube.utils.create_parameter(websocket, custom_param_name, '')
            custom_params.add(custom_param_name)
        
    print("Successfully Initialized")
