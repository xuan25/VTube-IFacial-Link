import math
import ifacial

FACE_POSITION_X_RATIO = 100
FACE_POSITION_Y_RATIO = 100
FACE_POSITION_Z_RATIO = 50

FACE_ANGLE_X_RATIO = 1
FACE_ANGLE_Y_RATIO = 1
FACE_ANGLE_Z_RATIO = 1

MOUTH_SMILE_RATIO = 2
MOUSE_OPEN_RATIO = 1.2

BROWS_RATIO = 2

TONGUE_OUT_RATIO = 0.4

EYE_OPEN_RATIO = 1.25
EYE_ROTATION_RATIO = 1.5

CHEEK_PUFF_RATIO = 2
FACE_ANGRY_RATIO = 0.3

BROW_LEFT_Y_RATIO = 2
BROW_RIGHT_Y_RATIO = 2

MOUTH_X_RATIO = 2


def build_params_dict(ifacial_data):
    ifacial_data = [
        # VTubeStudio Default
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
                                max(ifacial_data[ifacial.MOUTH_SMILE_LEFT] + ifacial_data[ifacial.MOUTH_SMILE_RIGHT] - 0.2, 0)                            # mouth smile (pos*2)
                                - math.pow(max(ifacial_data[ifacial.MOUTH_SHRUG_LOWER] - 0.4, 0), 1) * 1                                                  # mouth shrug (neg*1) (threshold: 0.4)
                                - math.pow(max((ifacial_data[ifacial.BROW_DOWN_LEFT] + ifacial_data[ifacial.BROW_DOWN_RIGHT]) / 2 - 0.3 + (0.08 + ((ifacial_data[ifacial.JAW_OPEN] - ifacial_data[ifacial.MOUTH_CLOSE]) * 0.15)), 0), 0.4) * 1.5    # brow low (neg*1.5) (threshold: 0.08 + mouth_open_factor)
                            ) * MOUTH_SMILE_RATIO                                                                       # ratio
                        ) / 2 + 0.5                                                                                     # range re-mapping
                    )
        },
        {
            "id": "MouthOpen",
            "value": (ifacial_data[ifacial.JAW_OPEN] - ifacial_data[ifacial.MOUTH_CLOSE]) * MOUSE_OPEN_RATIO
        },
        {
            "id": "Brows",
            "value": ifacial_data[ifacial.BROW_INNER_UP] * BROWS_RATIO
        },
        {
            "id": "TongueOut",
            "value": 0 if ifacial_data[ifacial.TONGUE_OUT] < TONGUE_OUT_RATIO else 1
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
            "value": 0 if ifacial_data[ifacial.MOUTH_ROLL_LOWER] * ifacial_data[ifacial.MOUTH_SHRUG_LOWER] < FACE_ANGRY_RATIO else 1
        },
        {
            "id": "BrowLeftY",
            "value": ((ifacial_data[ifacial.BROW_OUTER_UP_LEFT] - ifacial_data[ifacial.BROW_DOWN_LEFT]) * BROW_RIGHT_Y_RATIO + 1) / 2
        },
        {
            "id": "BrowRightY",
            "value": ((ifacial_data[ifacial.BROW_OUTER_UP_RIGHT] - ifacial_data[ifacial.BROW_DOWN_RIGHT]) * BROW_RIGHT_Y_RATIO + 1) / 2
        },
        {
            "id": "MouthX",
            "value": (ifacial_data[ifacial.MOUTH_LEFT] - ifacial_data[ifacial.MOUTH_RIGHT]) * MOUTH_X_RATIO
        },

        # ARKit
        {
            "id": "EyeBlinkLeft",
            "value": ifacial_data[ifacial.EYE_BLINK_LEFT]
        },
        {
            "id": "EyeLookDownLeft",
            "value": ifacial_data[ifacial.EYE_LOOK_DOWN_LEFT]
        },
        {
            "id": "EyeLookInLeft",
            "value": ifacial_data[ifacial.EYE_LOOK_IN_LEFT]
        },
        {
            "id": "EyeLookOutLeft",
            "value": ifacial_data[ifacial.EYE_LOOK_OUT_LEFT]
        },
        {
            "id": "EyeLookUpLeft",
            "value": ifacial_data[ifacial.EYE_LOOK_UP_LEFT]
        },
        {
            "id": "EyeSquintLeft",
            "value": ifacial_data[ifacial.EYE_SQUINT_LEFT]
        },
        {
            "id": "EyeWideLeft",
            "value": ifacial_data[ifacial.EYE_WIDE_LEFT]
        },
        {
            "id": "EyeBlinkRight",
            "value": ifacial_data[ifacial.EYE_BLINK_RIGHT]
        },
        {
            "id": "EyeLookDownRight",
            "value": ifacial_data[ifacial.EYE_LOOK_DOWN_RIGHT]
        },
        {
            "id": "EyeLookInRight",
            "value": ifacial_data[ifacial.EYE_LOOK_IN_RIGHT]
        },
        {
            "id": "EyeLookOutRight",
            "value": ifacial_data[ifacial.EYE_LOOK_OUT_RIGHT]
        },
        {
            "id": "EyeLookUpRight",
            "value": ifacial_data[ifacial.EYE_LOOK_UP_RIGHT]
        },
        {
            "id": "EyeSquintRight",
            "value": ifacial_data[ifacial.EYE_SQUINT_RIGHT]
        },
        {
            "id": "EyeWideRight",
            "value": ifacial_data[ifacial.EYE_WIDE_RIGHT]
        },
        {
            "id": "JawForward",
            "value": ifacial_data[ifacial.JAW_FORWARD]
        },
        {
            "id": "JawLeft",
            "value": ifacial_data[ifacial.JAW_LEFT]
        },
        {
            "id": "JawRight",
            "value": ifacial_data[ifacial.JAW_RIGHT]
        },
        {
            "id": "JawOpen",
            "value": ifacial_data[ifacial.JAW_OPEN]
        },
        {
            "id": "MouthClose",
            "value": ifacial_data[ifacial.MOUTH_CLOSE]
        },
        {
            "id": "MouthFunnel",
            "value": ifacial_data[ifacial.MOUTH_FUNNEL]
        },
        {
            "id": "MouthPucker",
            "value": ifacial_data[ifacial.MOUTH_PUCKER]
        },
        {
            "id": "MouthLeft",
            "value": ifacial_data[ifacial.MOUTH_LEFT]
        },
        {
            "id": "MouthRight",
            "value": ifacial_data[ifacial.MOUTH_RIGHT]
        },
        {
            "id": "MouthSmileLeft",
            "value": ifacial_data[ifacial.MOUTH_SMILE_LEFT]
        },
        {
            "id": "MouthSmileRight",
            "value": ifacial_data[ifacial.MOUTH_SMILE_RIGHT]
        },
        {
            "id": "MouthFrownLeft",
            "value": ifacial_data[ifacial.MOUTH_FROWN_LEFT]
        },
        {
            "id": "MouthFrownRight",
            "value": ifacial_data[ifacial.MOUTH_FROWN_RIGHT]
        },
        {
            "id": "MouthDimpleLeft",
            "value": ifacial_data[ifacial.MOUTH_DIMPLE_LEFT]
        },
        {
            "id": "MouthDimpleRight",
            "value": ifacial_data[ifacial.MOUTH_DIMPLE_RIGHT]
        },
        {
            "id": "MouthStretchLeft",
            "value": ifacial_data[ifacial.MOUTH_STRETCH_LEFT]
        },
        {
            "id": "MouthStretchRight",
            "value": ifacial_data[ifacial.MOUTH_STRETCH_RIGHT]
        },
        {
            "id": "MouthRollLower",
            "value": ifacial_data[ifacial.MOUTH_ROLL_LOWER]
        },
        {
            "id": "MouthRollUpper",
            "value": ifacial_data[ifacial.MOUTH_ROLL_UPPER]
        },
        {
            "id": "MouthShrugLower",
            "value": ifacial_data[ifacial.MOUTH_SHRUG_LOWER]
        },
        {
            "id": "MouthShrugUpper",
            "value": ifacial_data[ifacial.MOUTH_SHRUG_UPPER]
        },
        {
            "id": "MouthPressLeft",
            "value": ifacial_data[ifacial.MOUTH_PRESS_LEFT]
        },
        {
            "id": "MouthPressRight",
            "value": ifacial_data[ifacial.MOUTH_PRESS_RIGHT]
        },
        {
            "id": "MouthLowerDownLeft",
            "value": ifacial_data[ifacial.MOUTH_LOWER_DOWN_LEFT]
        },
        {
            "id": "MouthLowerDownRight",
            "value": ifacial_data[ifacial.MOUTH_LOWER_DOWN_RIGHT]
        },
        {
            "id": "MouthUpperUpLeft",
            "value": ifacial_data[ifacial.MOUTH_UPPER_UP_LEFT]
        },
        {
            "id": "MouthUpperUpRight",
            "value": ifacial_data[ifacial.MOUTH_UPPER_UP_RIGHT]
        },
        {
            "id": "BrowDownLeft",
            "value": ifacial_data[ifacial.BROW_DOWN_LEFT]
        },
        {
            "id": "BrowDownRight",
            "value": ifacial_data[ifacial.BROW_DOWN_RIGHT]
        },
        {
            "id": "BrowInnerUp",
            "value": ifacial_data[ifacial.BROW_INNER_UP]
        },
        {
            "id": "BrowOuterUpLeft",
            "value": ifacial_data[ifacial.BROW_OUTER_UP_LEFT]
        },
        {
            "id": "BrowOuterUpRight",
            "value": ifacial_data[ifacial.BROW_OUTER_UP_RIGHT]
        },
        {
            "id": "CheekPuff",
            "value": ifacial_data[ifacial.CHEEK_PUFF]
        },
        {
            "id": "CheekSquintLeft",
            "value": ifacial_data[ifacial.CHEEK_SQUINT_LEFT]
        },
        {
            "id": "CheekSquintRight",
            "value": ifacial_data[ifacial.CHEEK_SQUINT_RIGHT]
        },
        {
            "id": "NoseSneerLeft",
            "value": ifacial_data[ifacial.NOSE_SNEER_LEFT]
        },
        {
            "id": "NoseSneerRight",
            "value": ifacial_data[ifacial.NOSE_SNEER_RIGHT]
        },
        {
            "id": "TongueOut",
            "value": ifacial_data[ifacial.TONGUE_OUT]
        },
    ]
    return ifacial_data
