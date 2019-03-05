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

###### 

















