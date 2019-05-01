I created a first responder drone that is capable of real-time object 
detection and recording based on the mode I decide to put the drone in. 
The drone was originally supposed to have GPS implemented in it but the
specific model I have purchased sent my Pi into a kernel panic. Below
is an album of me building it and some late night flying. 

https://photos.app.goo.gl/owaxT1FffHMgUdnVA

In this project I used OpenCV to handle video and recording. 
I used TensorFlow for real-time object detection with the help
of Edje Electronics, Google, and dantitran's tutorials. 
I used knowledge gained from SJU's IoT class and the books that went
along with the course to handle the hardware. 
To learn about drones I read Getting Started with Drones by Kilby, Drones:
Make an Arduino Fly by McGriffy (Highly recommend), Building Drones for
the Evil Genius, and the YouTube channel Painless 360. 

Parts:
- S500 frame
- Raspberry Pi 3
- APM 2.8
- 3S 5200 mAh LiPo
- Readytosky 2212 motors
- DJI props
- Flycolor BLHeli_s 30A ESC
- Pi camera
- Logitech camera
- Two 5V UBECs
- FlySky i6X transmitter
- FlySky iA6B receiver
 
Below is an outline of where I thought I wanted to take the project below
earlier this semester. 





# Arduino-Based Drone
## To Do (No Order):


###### Software
- ~~Finish setting up TensorFlow and OpenCV on Pi~~
- Learn how to implement a Kalman Filter, Bayesian Filter, histogram filter, and particle filter
- Learn A * for Path Finding
- Potential Google Maps API integration (Time Dependent)

### Current Problems:

## Week One: 2/17 - 2/23
1. ~~Install TF & OpenCV~~
2. ~~Complete Make: Drones~~
3. ~~Calculate energy usage for project~~
	- ~~Learn how to read & create schematics~~
4. ~~Order parts [Work in Progress 2/26]~~
    - Calculate approximate kV and mAh for batteries
    - Still Need: Props, brushless motors, ESC, airframe, PDB, ArduPilot, telemetry radio, IMU, GPS, Bluetooth (optional), LiPo batteries
    - Have: Teensy 2.0, Arduino's, Raspberry Pi, wires, ultrasonic sensors, 3D printer for custom parts (time dependent)
5. ~~Get comfortable using APM Planner~~
6. ~~Determine main computer~~ 

###### Accomplishments: 
- Real-time object detection using OpenCV and TensorFlow
	- Program thought I was a cat
- Ordered list of parts
- Completed reading for project

###### Obstacles:
- Still unsure about hardware selection
	- Movidius, ODROID, Pine64, Tinkerboard, etc.
	- Most likely going to use Pi
- Power consumption
- Unable to wirelessly connect Pi to SJU network
- Drones cost a lot :(

## Week Two: 2/24 - 3/2
####### Main Focus: Hardware Basics
1. Make a "dumb" drone with parts
2. ~~Spend time on Fritzig~~
	- ~~Learn how to read and create schematics~~
    - ~~Create diagram~~
3. ~~Determine whether Movidius is worth it or not~~
4. Get started looking at Google Maps API with Pi
5. Implement A * with Google Maps API

## Week Three: 3/3 - 3/9
###### Redefine end goal: Smart Drone with Physics Abstracted Away or Simple, Dumb Drone?

Learn about PID, motors, yaw, pitch, filters (Kalman vs. Madgwick) & ArduPilot. 

### Smart Drone:
- ArduPilot: adds autonomous flying
- Less Electronic Parts (Everything is in ArduPilot)
- More Computational Power
- Easier
- Implements A* 

### Dumb Drone:
- No autonomy
- More Parts, More Customization
- Less Computational Power
- Harder Project

 
## Week 5 & 6: 3/10 - 3/23
###### What I've been working on...
Redefining the project:
- Smart drone for the time being
- May try to implement own flight controller

Assembled most of the parts, rest are on the way

Setting up TensorFlow and OpenCV for real time detection on boot
- consists of Bash and Python script

Potential Obstacles:
- Naze32 is hard to program or control; may need to use another flight controller that is more programmable
















