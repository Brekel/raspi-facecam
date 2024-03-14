# raspi-facecam

Scripts to download &amp; install [camera-streamer](https://github.com/ayufan/camera-streamer) for a [Raspberry Pi Zero 2](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w) with [Camera Module v3](https://www.raspberrypi.com/products/camera-module-3).

The primary use case is a wireless HMC (Helmet Mounted Camera) for facial motion capture.

For example the [Brekel Body v3 software](https://brekel.com/brekel-body-v3) can utilize this with it's face tracking functionality.


This is designed to be used in conjunction with a 3D printed case which can be downloaded from the following page (more info on bill of materials and assembly instructions there):
 [https://www.printables.com/model/805075-rasberry-pi-zero-face-camera](https://www.printables.com/model/805075-rasberry-pi-zero-face-camera)
![exploded_case](images/exploded_case.png)
![bill of materials](images/BOM.png)



## Installation
git clone https://github.com/Brekel/raspi-facecam.git

cd raspi-facecam

chmod +x install_camera-streamer.sh

./install_camera-streamer.sh