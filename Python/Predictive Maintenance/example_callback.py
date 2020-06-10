#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "6qX3zX" # Change XXYYZZ to the UID of your Servo Brick

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_servo import BrickServo

# Use position reached callback to swing back and forth
def cb_position_reached(servo_num, position):
    print('hello')
    if position == 4500:
        print('Position: 90°, going to -90°')
        servo.set_position(servo_num, -4500)
    elif position == -4500:
        print('Position: -90°, going to 90°')
        servo.set_position(servo_num, 4500)
    else:
        print('Error') # Can only happen if another program sets position

while True:
    ipcon = IPConnection() # Create IP connection
    servo = BrickServo(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected
    print(1)
    # Register position reached callback to function cb_position_reached
    servo.register_callback(servo.CALLBACK_POSITION_REACHED, cb_position_reached)

    # Enable position reached callback
    servo.enable_position_reached_callback()

    # Set velocity to 100°/s. This has to be smaller or equal to the
    # maximum velocity of the servo you are using, otherwise the position
    # reached callback will be called too early
    servo.set_output_voltage(6000)

    servo.set_degree(0, -4500, 4500)
    servo.set_pulse_width(0, 1000, 2000)
    servo.set_period(0, 19500)
    servo.set_acceleration(0, 10000)  # acceleration
    servo.set_velocity(0, 20000)

    servo.set_position(0, 4500)
    servo.enable(0)

    print(2)

    input("Press key to exit\n") # Use input() in Python 3
    servo.disable(0)
    ipcon.disconnect()
