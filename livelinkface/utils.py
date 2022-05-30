import math
from livelinkface.pylivelinkface import FaceBlendShape, PyLiveLinkFace

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

EYE_OPEN_RATIO = 1.5
EYE_ROTATION_RATIO = 1.5

CHEEK_PUFF_RATIO = 2
FACE_ANGRY_RATIO = 0.3

BROW_LEFT_Y_RATIO = 2
BROW_RIGHT_Y_RATIO = 2

MOUTH_X_RATIO = 2


def build_params_dict(raw_data: PyLiveLinkFace):
    data = [
        {
            "id": "FacePositionX",
            "value": 0 * FACE_POSITION_X_RATIO
        },
        {
            "id": "FacePositionY",
            "value": 0 * FACE_POSITION_Y_RATIO
        },
        {
            "id": "FacePositionZ",
            "value": 0 * FACE_POSITION_Z_RATIO
        },
        {
            "id": "FaceAngleX",
            "value": raw_data.get_blendshape(FaceBlendShape.HeadPitch) * FACE_ANGLE_X_RATIO
        },
        {
            "id": "FaceAngleY",
            "value": raw_data.get_blendshape(FaceBlendShape.HeadYaw) * FACE_ANGLE_Y_RATIO
        },
        {
            "id": "FaceAngleZ",
            "value": raw_data.get_blendshape(FaceBlendShape.HeadRoll) * FACE_ANGLE_Z_RATIO
        },
        {
            "id": "MouthSmile",
            "value": (
                        (
                            (
                                max(raw_data.get_blendshape(FaceBlendShape.MouthSmileLeft) + raw_data.get_blendshape(FaceBlendShape.MouthSmileRight) - 0.2, 0)                            # mouth smile (pos*2)
                                - math.pow(max(raw_data.get_blendshape(FaceBlendShape.MouthShrugLower) - 0.4, 0), 1) * 1                                                  # mouth shrug (neg*1) (threshold: 0.4)
                                - math.pow(max(-raw_data.get_blendshape(FaceBlendShape.BrowInnerUp) + (0.08 + (raw_data.get_blendshape(FaceBlendShape.JawOpen) * 0.15)), 0), 0.4) * 1.5    # brow low (neg*1.5) (threshold: 0.08 + mouth_open_factor)
                            ) * MOUTH_SMILE_RATIO                                                                       # ratio
                        ) / 2 + 0.5                                                                                     # range re-mapping
                    )
        },
        {
            "id": "MouthOpen",
            "value": raw_data.get_blendshape(FaceBlendShape.JawOpen) * MOUSE_OPEN_RATIO
        },
        {
            "id": "Brows",
            "value": raw_data.get_blendshape(FaceBlendShape.BrowInnerUp) * BROWS_RATIO
        },
        {
            "id": "TongueOut",
            "value": 0 if raw_data.get_blendshape(FaceBlendShape.TongueOut) < TONGUE_OUT_RATIO else 1
        },
        {
            "id": "EyeOpenLeft",
            "value": (1 - raw_data.get_blendshape(FaceBlendShape.EyeBlinkLeft)) * EYE_OPEN_RATIO - (EYE_OPEN_RATIO - 1)
        },
        {
            "id": "EyeOpenRight",
            "value": (1 - raw_data.get_blendshape(FaceBlendShape.EyeBlinkRight)) * EYE_OPEN_RATIO - (EYE_OPEN_RATIO - 1)
        },
        {
            "id": "EyeLeftX",
            "value": (raw_data.get_blendshape(FaceBlendShape.EyeLookInLeft) - raw_data.get_blendshape(FaceBlendShape.EyeLookOutLeft)) * EYE_ROTATION_RATIO
        },
        {
            "id": "EyeLeftY",
            "value": (raw_data.get_blendshape(FaceBlendShape.EyeLookUpLeft) - raw_data.get_blendshape(FaceBlendShape.EyeLookDownLeft)) * EYE_ROTATION_RATIO
        },
        {
            "id": "EyeRightX",
            "value": (raw_data.get_blendshape(FaceBlendShape.EyeLookOutRight) - raw_data.get_blendshape(FaceBlendShape.EyeLookInRight)) * EYE_ROTATION_RATIO
        },
        {
            "id": "EyeRightY",
            "value": (raw_data.get_blendshape(FaceBlendShape.EyeLookUpRight) - raw_data.get_blendshape(FaceBlendShape.EyeLookDownRight)) * EYE_ROTATION_RATIO
        },
        {
            "id": "CheekPuff",
            "value": raw_data.get_blendshape(FaceBlendShape.CheekPuff) * CHEEK_PUFF_RATIO
        },
        {
            "id": "FaceAngry",
            "value": 0 if raw_data.get_blendshape(FaceBlendShape.MouthRollLower) * raw_data.get_blendshape(FaceBlendShape.MouthShrugLower) < FACE_ANGRY_RATIO else 1
        },
        {
            "id": "BrowLeftY",
            "value": raw_data.get_blendshape(FaceBlendShape.BrowOuterUpLeft) * BROW_LEFT_Y_RATIO
        },
        {
            "id": "BrowRightY",
            "value": raw_data.get_blendshape(FaceBlendShape.EyeLookInRight) * BROW_RIGHT_Y_RATIO
        },
        {
            "id": "MouthX",
            "value": (raw_data.get_blendshape(FaceBlendShape.MouthLeft) - raw_data.get_blendshape(FaceBlendShape.MouthRight)) * MOUTH_X_RATIO
        },
    ]
    return data
