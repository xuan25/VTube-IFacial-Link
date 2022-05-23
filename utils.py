import math
import ifacial

FACE_POSITION_X_RATIO = 100
FACE_POSITION_Y_RATIO = 100
FACE_POSITION_Z_RATIO = 20

FACE_ANGLE_X_RATIO = 1
FACE_ANGLE_Y_RATIO = 1
FACE_ANGLE_Z_RATIO = 1

MOUTH_SMILE_RATIO = 3
MOUSE_OPEN_RATIO = 1.5

BROWS_RATIO = 2

TONGUE_OUT_RATIO = 10

EYE_OPEN_RATIO = 1.5
EYE_ROTATION_RATIO = 1.5

CHEEK_PUFF_RATIO = 2
FACE_ANGRY_RATIO = 2

BROW_LEFT_Y_RATIO = 2
BROW_RIGHT_Y_RATIO = 2

MOUTH_X_RATIO = 2


def build_params_dict(ifacial_data):
    ifacial_data = [
        {
            "id": "FacePositionX",
            "value": ifacial_data[ifacial.HEAD_POSITION_X] * FACE_POSITION_X_RATIO
        },
        {
            "id": "FacePositionY",
            "value": ifacial_data[ifacial.HEAD_POSITION_Y] * FACE_POSITION_Y_RATIO
        },
        {
            "id": "FacePositionZ",
            "value": -ifacial_data[ifacial.HEAD_POSITION_Z] * FACE_POSITION_Z_RATIO
        },
        {
            "id": "FaceAngleX",
            "value": ifacial_data[ifacial.HEAD_ROTATION_Y] * FACE_ANGLE_X_RATIO
        },
        {
            "id": "FaceAngleY",
            "value": -ifacial_data[ifacial.HEAD_ROTATION_X] * FACE_ANGLE_Y_RATIO
        },
        {
            "id": "FaceAngleZ",
            "value": -ifacial_data[ifacial.HEAD_ROTATION_Z] * FACE_ANGLE_Z_RATIO
        },
        {
            "id": "MouthSmile",
            "value": (
                        (
                            (
                                (ifacial_data[ifacial.MOUTH_SMILE_LEFT] + ifacial_data[ifacial.MOUTH_SMILE_RIGHT])      # mouth smile (pos)
                                - ifacial_data[ifacial.MOUTH_SHRUG_LOWER]                                               # mouth shrug (neg)
                            ) * MOUTH_SMILE_RATIO                                                                       # ratio
                        ) / 2 + 0.5                                                                                     # range re-mapping
                        - (math.pow(ifacial_data[ifacial.JAW_OPEN], 0.4) * 1)                                           # mouth open correction (neg; sad component)
                    )
        },
        {
            "id": "MouthOpen",
            "value": ifacial_data[ifacial.JAW_OPEN] * MOUSE_OPEN_RATIO
        },
        {
            "id": "Brows",
            "value": ifacial_data[ifacial.BROW_INNER_UP] * BROWS_RATIO
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
            "value": (ifacial_data[ifacial.EYE_LOOK_IN_LEFT] - ifacial_data[ifacial.EYE_LOOK_OUT_LEFT]) * EYE_ROTATION_RATIO
        },
        {
            "id": "EyeLeftY",
            "value": (ifacial_data[ifacial.EYE_LOOK_UP_LEFT] - ifacial_data[ifacial.EYE_LOOK_DOWN_LEFT]) * EYE_ROTATION_RATIO
        },
        {
            "id": "EyeRightX",
            "value": (ifacial_data[ifacial.EYE_LOOK_OUT_RIGHT] - ifacial_data[ifacial.EYE_LOOK_IN_RIGHT]) * EYE_ROTATION_RATIO
        },
        {
            "id": "EyeRightY",
            "value": (ifacial_data[ifacial.EYE_LOOK_UP_RIGHT] - ifacial_data[ifacial.EYE_LOOK_DOWN_RIGHT]) * EYE_ROTATION_RATIO
        },
        {
            "id": "CheekPuff",
            "value": ifacial_data[ifacial.CHEEK_PUFF] * CHEEK_PUFF_RATIO
        },
        {
            "id": "FaceAngry",
            "value": ifacial_data[ifacial.MOUTH_ROLL_LOWER] * FACE_ANGRY_RATIO
        },
        {
            "id": "BrowLeftY",
            "value": ifacial_data[ifacial.BROW_OUTER_UP_LEFT] * BROW_LEFT_Y_RATIO
        },
        {
            "id": "BrowRightY",
            "value": ifacial_data[ifacial.BROW_OUTER_UP_RIGHT] * BROW_RIGHT_Y_RATIO
        },
        {
            "id": "MouthX",
            "value": (ifacial_data[ifacial.MOUTH_LEFT] - ifacial_data[ifacial.MOUTH_RIGHT]) * MOUTH_X_RATIO
        },
    ]
    return ifacial_data
