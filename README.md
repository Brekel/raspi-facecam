# raspi-facecam

Scripts to download &amp; install [camera-streamer](https://github.com/ayufan/camera-streamer) and apply optimal settings for a [Raspberry Pi Zero 2](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w) with [Camera Module v3](https://www.raspberrypi.com/products/camera-module-3) to live stream video data at the highest possible frame rate.


The primary use case is as a wireless HMC (Helmet Mounted Camera) for facial motion capture.
For example the [Brekel Body v3 software](https://brekel.com/brekel-body-v3) can utilize this with it's face tracking functionality.


This is designed to be used with a 3D printed case that can be downloaded from the following page (more info on bill of materials and assembly instructions there):
 [https://www.printables.com/model/805075-rasberry-pi-zero-face-camera](https://www.printables.com/model/805075-rasberry-pi-zero-face-camera)
![exploded_case](images/exploded_case.png)
![bill of materials](images/BOM.png)



## Installation
* Use the Raspberry Pi Imager to install the 64-bit Lite version of Raspberry Pi OS
* Make sure to configure your WiFi settings using the "Edit Settings" option and enable SSH
* Once completed you can insert the SD-Card into the Pi through the side hole, you may need a small screw driver or tweezers to carefully slide it into place (this was deliberately designed so it takes some effort to remove)
* SSH into your Pi and run the following commands to download and install the software:
```bash
git clone https://github.com/Brekel/raspi-facecam.git
cd raspi-facecam
chmod +x install_camera-streamer.sh
./install_camera-streamer.sh
```
  