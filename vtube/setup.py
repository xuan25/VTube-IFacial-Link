import json
import os

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

    print("Successfully Initialized")
