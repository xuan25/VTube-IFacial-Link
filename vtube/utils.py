import json

import vtube


async def request_token(websocket):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": vtube.API_VERSION,
        "requestID": vtube.REQUEST_ID,
        "messageType": "AuthenticationTokenRequest",
        "data": {
            "pluginName": vtube.PLUGIN_NAME,
            "pluginDeveloper": vtube.PLUGIN_DEVELOPER,
        }
    }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    authtoken = pack['data']['authenticationToken']
    return authtoken


async def register_plugin(websocket, authtoken):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": vtube.API_VERSION,
        "requestID": vtube.REQUEST_ID,
        "messageType": "AuthenticationRequest",
        "data": {
            "pluginName": vtube.PLUGIN_NAME,
            "pluginDeveloper": vtube.PLUGIN_DEVELOPER,
            "authenticationToken": authtoken
        }
    }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack


async def list_parameters(websocket):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": vtube.API_VERSION,
        "requestID": vtube.REQUEST_ID,
        "messageType": "InputParameterListRequest"
    }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack


async def create_parameter(websocket, parameterName, explanation, min=0, max=1, defaultValue=0):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": vtube.API_VERSION,
        "requestID": vtube.REQUEST_ID,
        "messageType": "ParameterCreationRequest",
        "data": {
            "parameterName": parameterName,
            "explanation": explanation,
            "min": min,
            "max": max,
            "defaultValue": defaultValue
        }
    }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack


async def inject_params(websocket, parameter_values):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "SomeID",
        "messageType": "InjectParameterDataRequest",
        "data": {
            "faceFound": True,
            "parameterValues": parameter_values
        }
    }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack
