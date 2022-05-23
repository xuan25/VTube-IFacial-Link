# VTube-IFacial-Link

A *VtubeStudio* plugin that bridging facial capture from *iFacialMocap* (IOS), enabling full apple ARkit facial tracking features.

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
