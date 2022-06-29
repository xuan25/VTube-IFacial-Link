# VTube-IFacial-Link

[简体中文](./README-zh-cn.md)

A *VTube Studio* plugin that bridging facial tracking from *iFacialMocap* (IOS), enabling full apple ARKit facial tracking features.

| ![](imgs/screenshot1.png) | ![](imgs/screenshot2.png) |
|---|---|

## Quick Start Guide

*Note: The program is developed on Python 3.8.10*

1. Clone the repository.
2. Run command `pip install -r requirements.txt` to restore all the dependencies.
3. Make sure both your iPhone and PC are on the same network.
4. Launch both VtubeStudio on your PC and iFacialMocap on your iPhone.
5. Make sure the `VTube Studio API` is enabled, where the port should be 8001.
6. Launch the Bridging Plugin by command `python main.py -c <iPhone's IP Address>`, where `<iPhone's IP Address>` is the address shown in the iFacialMocap.
7. You should see a window showing all of the captured parameters and VtubeStudio should detect the plugin. 

## Supported Parameters

### VTube Studio Default

- FacePositionX
- FacePositionY
- FacePositionZ
- FaceAngleX
- FaceAngleY
- FaceAngleZ
- MouthSmile
- MouthOpen
- Brows
- TongueOut
- EyeOpenLeft
- EyeOpenRight
- EyeLeftX
- EyeLeftY
- EyeRightX
- EyeRightY
- CheekPuff
- FaceAngry
- BrowLeftY
- BrowRightY
- MouthX

### Custom Parameters (ARKit)

- EyeBlinkLeft
- EyeLookDownLeft
- EyeLookInLeft
- EyeLookOutLeft
- EyeLookUpLeft
- EyeSquintLeft
- EyeWideLeft
- EyeBlinkRight
- EyeLookDownRight
- EyeLookInRight
- EyeLookOutRight
- EyeLookUpRight
- EyeSquintRight
- EyeWideRight
- JawForward
- JawLeft
- JawRight
- JawOpen
- MouthClose
- MouthFunnel
- MouthPucker
- MouthLeft
- MouthRight
- MouthSmileLeft
- MouthSmileRight
- MouthFrownLeft
- MouthFrownRight
- MouthDimpleLeft
- MouthDimpleRight
- MouthStretchLeft
- MouthStretchRight
- MouthRollLower
- MouthRollUpper
- MouthShrugLower
- MouthShrugUpper
- MouthPressLeft
- MouthPressRight
- MouthLowerDownLeft
- MouthLowerDownRight
- MouthUpperUpLeft
- MouthUpperUpRight
- BrowDownLeft
- BrowDownRight
- BrowInnerUp
- BrowOuterUpLeft
- BrowOuterUpRight
- CheekPuff
- CheekSquintLeft
- CheekSquintRight
- NoseSneerLeft
- NoseSneerRight
- TongueOut

## Roadmap

- [ ] Use ML model to detect smiling and anger from multiple parameters.
- [ ] Build a standalone face tracking link app on IOS. [ref](https://developer.apple.com/documentation/arkit/content_anchors/tracking_and_visualizing_faces)
- [ ] Hand tracking feature [ref-1](https://developer.apple.com/videos/play/wwdc2020/10653/) [ref-2](https://developer.apple.com/documentation/vision/detecting_hand_poses_with_vision)

## Acknowledgment

The model in screenshots is created by [猫旦那](https://www.bilibili.com/video/BV1yo4y1f7Xe)
