"""
Run this script
"""
import sys
import select
from motor_driver import DualMotorDriver
from time import sleep


# SETUP
bot = DualMotorDriver(left_pins=(None, None, None), right_pins=(None, None, None))
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
event = poller.poll()


# LOOP
while True:
    for msg, _ in event:
        buffer = msg.readline().rstrip()  # range of interest
        # print(buffer)  # this will transmit buffer back to RPi
        
