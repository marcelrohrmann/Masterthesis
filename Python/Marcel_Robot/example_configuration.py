#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "6qX3zX" # Change XXYYZZ to the UID of your Stepper Brick

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_servo import BrickServo

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    servo = BrickServo(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Configure two servos with voltage 6V

    servo.set_output_voltage(6000)

    servo.set_degree(0, -9000, 9000)
    servo.set_pulse_width(0, 1000, 2000)
    servo.set_period(0, 20000)
    servo.set_acceleration(0, 2000) # Slow acceleration
    servo.set_velocity(0, 10000) # Full speed

    servo.set_degree(1, -9000, 9000)
    servo.set_pulse_width(1, 500, 2500)
    servo.set_period(1, 20000)
    servo.set_acceleration(1, 2000)  # Slow acceleration
    servo.set_velocity(1, 10000)  # Full speed

    servo.set_degree(2, -9000, 9000)
    servo.set_pulse_width(2, 500, 2500)
    servo.set_period(2, 20000)
    servo.set_acceleration(2, 2000)  # Slow acceleration
    servo.set_velocity(2, 10000)  # Full speed

    servo.set_degree(3, -9000, 9000)
    servo.set_pulse_width(3, 1000, 2000)
    servo.set_period(3, 20000)
    servo.set_acceleration(3, 2000)  # Slow acceleration
    servo.set_velocity(3, 10000)  # Full speed

    servo.set_degree(4, -9000, 9000)
    servo.set_pulse_width(4, 500, 2500)
    servo.set_period(4, 20000)
    servo.set_acceleration(4, 2000) # Slow acceleration
    servo.set_velocity(4, 10000) # Full speed

    servo.set_degree(5, -9000, 9000)
    servo.set_pulse_width(5, 500, 2500)
    servo.set_period(5, 20000)
    servo.set_acceleration(5, 2000)  # Slow acceleration
    servo.set_velocity(5, 10000)  # Full speed

    servo.set_degree(6, -9000, 9000)
    servo.set_pulse_width(6, 500, 2500)
    servo.set_period(6, 20000)
    servo.set_acceleration(6, 2000)  # Slow acceleration
    servo.set_velocity(6, 10000)  # Full speed

    servo.set_position(0, -1000) # Set to most right position
    servo.enable(0)

    servo.set_position(1, -2000)  # Set to most right position
    servo.enable(1)

    servo.set_position(2, 2000)  # Set to most right position
    servo.enable(2)

    servo.set_position(3, -3000)  # Set to most right position
    servo.enable(3)

    servo.set_position(4, -6000) # Set to most left position
    servo.enable(4)

    servo.set_position(5, -6000)  # Set to most left position
    servo.enable(5)

    servo.set_position(6, 0)  # Set to most left position
    servo.enable(6)


    input("Press key to exit\n") # Use input() in Python 3
    servo.disable(0)
    servo.disable(1)
    servo.disable(2)
    servo.disable(3)
    servo.disable(4)
    servo.disable(5)
    servo.disable(6)
    ipcon.disconnect()