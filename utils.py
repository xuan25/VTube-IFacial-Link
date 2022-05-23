import math
import ifacial

POSITION_X_RATIO = 100
POSITION_Y_RATIO = 100
POSITION_Z_RATIO = 20
TONGUE_OUT_RATIO = 10
MOUSE_SMILE_RATIO = 2
MOUSE_SMILE_OFFSET = 0.3
MOUSE_OPEN_RATIO = 1
EYE_OPEN_RATIO = 2

def build_params_dict(ifacial_data):
    ifacial_data = [
        {
            "id": "FacePositionX",
            "value": ifacial_data[ifacial.HEAD_POSITION_X] * POSITION_X_RATIO
        },
        {
            "id": "FacePositionY",
            "value": ifacial_data[ifacial.HEAD_POSITION_Y] * POSITION_Y_RATIO
        },
        {
            "id": "FacePositionZ",
            "value": -ifacial_data[ifacial.HEAD_POSITION_Z] * POSITION_Z_RATIO
        },
        {
            "id": "FaceAngleX",
            "value": ifacial_data[ifacial.HEAD_ROTATION_Y]
        },
        {
            "id": "FaceAngleY",
            "value": -ifacial_data[ifacial.HEAD_ROTATION_X]
        },
        {
            "id": "FaceAngleZ",
            "value": -ifacial_data[ifacial.HEAD_ROTATION_Z]
        },
        {
            "id": "MouthSmile",
            "value": (
                        (
                            (ifacial_data[ifacial.MOUTH_SMILE_LEFT] + ifacial_data[ifacial.MOUTH_SMILE_RIGHT]) / 2 * MOUSE_SMILE_RATIO  # mouth smile (pos)
                            - ifacial_data[ifacial.MOUTH_SHRUG_LOWER] * MOUSE_SMILE_RATIO                                               # mouth shrug (neg)
                        ) / 2 + 0.5 + MOUSE_SMILE_OFFSET                                                                                # ratio
                        - (math.pow(ifacial_data[ifacial.JAW_OPEN], 0.1) * 0.5)             # mouth open correction (neg; sad component)
                    )
        },
        {
            "id": "MouthOpen",
            "value": ifacial_data[ifacial.JAW_OPEN] * MOUSE_OPEN_RATIO
        },
        {
            "id": "Brows",
            "value": ifacial_data[ifacial.BROW_INNER_UP]
        },
        {
            "id": "TongueOut",
            "value": ifacial_data[ifacial.TONGUE_OUT] * TONGUE_OUT_RATIO
        },
        {
            "id": "EyeOpenLeft",
            "value": (1 - ifacial_data[ifacial.EYE_BLINK_LEFT]) * EYE_OPEN_RATIO - (EYE_OPEN_RATIO - 1)
        },
        {
            "id": "EyeOpenRight",
            "value": (1 - ifacial_data[ifacial.EYE_BLINK_RIGHT]) * EYE_OPEN_RATIO - (EYE_OPEN_RATIO - 1)
        },
        {
            "id": "EyeLeftX",
            "value": ifacial_data[ifacial.EYE_LOOK_IN_LEFT] - ifacial_data[ifacial.EYE_LOOK_OUT_LEFT]
        },
        {
            "id": "EyeLeftY",
            "value": ifacial_data[ifacial.EYE_LOOK_UP_LEFT] - ifacial_data[ifacial.EYE_LOOK_DOWN_LEFT]
        },
        {
            "id": "EyeRightX",
            "value": ifacial_data[ifacial.EYE_LOOK_OUT_RIGHT] - ifacial_data[ifacial.EYE_LOOK_IN_RIGHT]
        },
        {
            "id": "EyeRightY",
            "value": ifacial_data[ifacial.EYE_LOOK_UP_RIGHT] - ifacial_data[ifacial.EYE_LOOK_DOWN_RIGHT]
        },
        {
            "id": "CheekPuff",
            "value": 0
        },
        {
            "id": "FaceAngry",
            "value": 0
        },
        {
            "id": "BrowLeftY",
            "value": ifacial_data[ifacial.BROW_OUTER_UP_LEFT]
        },
        {
            "id": "BrowRightY",
            "value": ifacial_data[ifacial.BROW_OUTER_UP_RIGHT]
        },
        {
            "id": "MouthX",
            "value": 0
        },
    ]
    return ifacial_data
