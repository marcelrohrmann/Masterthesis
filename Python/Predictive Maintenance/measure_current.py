
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

HEADER = ['t', 'current']

def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)
    time0 = time.time()
    t = 0

    while t <= 10:
        current = servo.get_servo_current(0)
        csv_writer.writerow([round(t, 2), current])
        csvfile.flush()
        time.sleep(0.05)
        t = t + 0.05

data_counter = 9

csv_name = "servo_current_NOK_{}.csv".format(data_counter)

with open(csv_name, 'w', newline='') as csvfile:
    processing_loop(csvfile)




