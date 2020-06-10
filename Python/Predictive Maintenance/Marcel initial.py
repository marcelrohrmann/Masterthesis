#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "6qX3zX" # Change XXYYZZ to the UID of your Servo Brick

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_servo import BrickServo

while True:
    ipcon = IPConnection() # Create IP connection
    servo = BrickServo(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Configure two servos with voltage 5.5V
    # Servo 1: Connected to port 0, period of 19.5ms, pulse width of 1 to 2ms
    #          and operating angle -100 to 100°
    #
    # Servo 2: Connected to port 5, period of 20ms, pulse width of 0.95
    #          to 1.95ms and operating angle -90 to 90°
    servo.set_output_voltage(6000)

    servo.set_degree(0, -4500, 4500)
    servo.set_pulse_width(0, 1000, 2000)
    servo.set_period(0, 20000)
    servo.set_acceleration(0, 10000) # Slow acceleration
    servo.set_velocity(0, 20000) # Full speed

    servo.enable(0)



