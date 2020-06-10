
HOST = "localhost"
PORT = 4223
UID = "6qX3zX" # Change XXYYZZ to the UID of your Servo Brick
import time
import csv
import datetime

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_servo import BrickServo

ipcon = IPConnection()  # Create IP connection
servo = BrickServo(UID, ipcon)  # Create device object

ipcon.connect(HOST, PORT)  # Connect to brickd

servo.set_output_voltage(6000)
servo.set_degree(0, -4500, 4500)
servo.set_pulse_width(0, 1000, 2000)
servo.set_period(0, 20000)
servo.set_acceleration(0, 10000)  # Slow acceleration
servo.set_velocity(0, 20000)  # Full speed

HEADER = ['t', 'current', 'position', 'velocity', 'chip_temp']

def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)
    time0 = time.time()
    t = 0

    while t <= 10:
        current = servo.get_servo_current(0)
        position = servo.get_current_position(0)
        velocity = servo.get_current_velocity(0)
        chip_temp = servo.get_chip_temperature()/10  #temp in Celsius

        csv_writer.writerow([round(t, 2), current, position, velocity, round(chip_temp,4)])
        csvfile.flush()
        time.sleep(0.05)
        t = t + 0.05

data_counter = 0

csv_name = "servo_data_all_{}.csv".format(data_counter)

with open(csv_name, 'w', newline='') as csvfile:
    processing_loop(csvfile)




