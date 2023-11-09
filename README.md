# Wall Following 
Drive your robot to follow the wall that was used in [Project 2](https://classroom.github.com/a/uu6PHG7i) with the help of the [RPlidar A1](https://www.slamtec.ai/home/rplidar_a1/) sensor. 

## Instructions:
1. (45% **On Raspberry Pi computer**) Scan the distance from your robot to the adjacent wall. Transmit appropriate data to Pico board using serial communication.
2. (45% **On Pico board**) Read the data transmitted from RPi computer, spin motors with tailored speed (and direction) based on the data. Your robot should move forward while maintain a resonable range to the wall on only one side (either left or right, but not both).  

> Hints:
> 1. Take a look at the range scan at about +/- 45 degrees.
> 2. Lidar may not be able to detect anything if wall is closer than 0.3 meters.
> 3. You can spin motors at different speed and direction.

2. (10%) Upload a video which records **at least 2 cycles** of wall following. 

