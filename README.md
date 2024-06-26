# raspi-facecam

Scripts to download &amp; install [camera-streamer](https://github.com/ayufan/camera-streamer) and apply optimal settings for a [Raspberry Pi Zero 2W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w) with [Camera Module v3](https://www.raspberrypi.com/products/camera-module-3) to live stream video data at the highest possible frame rate.


The primary use case is as a wireless HMC (Helmet Mounted Camera) for facial motion capture.  
For example the [Brekel Body v3 software](https://brekel.com/brekel-body-v3) can utilize this with it's face tracking functionality.


This is designed to be used with a 3D printed case that can be downloaded from the following page(s) (more info on bill of materials and assembly instructions there):  
[Printables](https://www.printables.com/model/805075-rasberry-pi-zero-face-camera)  
[MakerWorld](https://makerworld.com/en/models/387990)  
![exploded_case](images/exploded_case.png)
![bill of materials](images/BOM.png)



## Installation
(you can find a more step-by step guide in the PDF from the documentation folder)

* Use the Raspberry Pi Imager to install the 64-bit Lite version of Raspberry Pi OS
* Make sure to configure your WiFi settings using the "Edit Settings" option and enable SSH
* Once completed you can insert the SD-Card into the Pi through the side hole, you may need a small screw driver or tweezers to carefully slide it into place (this was deliberately designed so it takes some effort to remove)
* SSH into your Pi

### run the following commands to make sure git is available (only needed once on initial installation)
```bash
sudo apt install -y git
```

### run the following commands to download &amp; install the software (or if you want to update things in the future)
```bash
git clone https://github.com/Brekel/raspi-facecam.git
cd raspi-facecam
./install_camera-streamer.sh
```

Installation can take 5-10 minutes (depending on your SD-card and internet speed)
When finished you can access the video stream over the listed http listed in the console.


## Update
When you want to update to the latest version
* SSH into your Pi
* use the following command to remove the current files:
```bash
rm -rf raspi-facecam
```
* clone the github repo again and run the installation script again (same as above for initial install)
```bash
git clone https://github.com/Brekel/raspi-facecam.git
cd raspi-facecam
./install_camera-streamer.sh
```

## HMC (Helmet Mounted Camera) mounting solution

The 3D printed case can be attached to a helmet using standard GoPro mounting hardware like this:
![HMC GoPro](images/HMC_GoPro.jpg)

Another, more sophisticated option is to to attach it using some additional 3D prints and a carbon rod:
![HMC1](images/HMC.jpg)
The advantage of this solution is that it’s fully adjustable, it can be adjusted by pivoting on two axis and the distance of the camera to the face can be adjusted as well.

3D printable files can be found here:  
[Printables](https://www.printables.com/model/823454-hmc-helmet-mounted-camera-mounting-solution)  
[MakerWorld](https://makerworld.com/en/models/400309)