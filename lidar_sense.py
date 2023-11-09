"""
Run this script on RPi computer
"""
from math import floor
from adafruit_rplidar import RPLidar
import serial


# SETUP
ser = serial.Serial('/dev/ttyACM0', 115200)
lidar = RPLidar(motor_pin=None, port='/dev/ttyUSB0', timeout=3)
# min_scan_size = 120


# LOOP
try:
    for scan in lidar.iter_scans():
        # Transmit scan data
        if len(scan) > min_scan_size:
            pass
        # Read feedback from pico, useful for debugging
        # if ser.inWaiting() > 0:
        #     pico_data = ser.readline()
        #     pico_data = pico_data.decode("utf-8", "ignore")
        #     print(pico_data)
# Press "Ctrl c" to terminate 
except KeyboardInterrupt:
    print("Stopping.")
lidar.stop_motor()
lidar.stop()
lidar.disconnect()
