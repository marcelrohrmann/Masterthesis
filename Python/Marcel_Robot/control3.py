HOST = "localhost"
PORT = 4223
UID = "6qX3zX" # Change XXYYZZ to the UID of your Stepper Brick

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_servo import BrickServo
import keyboard


if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    servo = BrickServo(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd

    servo.set_output_voltage(6000)

    servo.set_degree(0, -9000, 9000)
    servo.set_pulse_width(0, 750, 2050) #PWM enspricht +90 -90 Pos.  Set.Positon(0,0) = ist mitte von tisch
    servo.set_period(0, 19500)
    servo.set_acceleration(0, 2000)  # Slow acceleration
    servo.set_velocity(0, 10000)  # Full speed

    servo.set_degree(1, -9000, 9000)
    servo.set_pulse_width(1, 500, 2500)
    servo.set_period(1, 19500)
    servo.set_acceleration(1, 2000)  # Slow acceleration
    servo.set_velocity(1, 10000)  # Full speed

    servo.set_degree(2, -9000, 9000)
    servo.set_pulse_width(2, 500, 2500)
    servo.set_period(2, 19500)
    servo.set_acceleration(2, 2000)  # Slow acceleration
    servo.set_velocity(2, 10000)  # Full speed

    #arm 2
    servo.set_degree(3, -11000, 0)  #-11000 arm2 down, 0 arm2 up
    servo.set_pulse_width(3, 1000, 2000)
    servo.set_period(3, 19500)
    servo.set_acceleration(3, 2000)  # Slow acceleration
    servo.set_velocity(3, 10000)  # Full speed

    # rotate arm2, not important, defect
    servo.set_degree(4, -9000, 9000)
    servo.set_pulse_width(4, 1000, 2000)
    servo.set_period(4, 19500)
    servo.set_acceleration(4, 2000)  # Slow acceleration
    servo.set_velocity(4, 10000)  # Full speed

    #0 gripper down, 3000 gripper up limit(ca.30°)
    servo.set_degree(5, 0, 3000)  #kleiner winkelbereich. Damit nicht crasht mit camera
    servo.set_pulse_width(5, 700, 1000)
    servo.set_period(5, 19500)
    servo.set_acceleration(5, 2000)  # Slow acceleration
    servo.set_velocity(5, 10000)  # Full speed

    # fixed value for gripper
    servo.set_degree(6, -10000, 0) #-10 000 geschlossen, 0 offen
    servo.set_pulse_width(6, 800, 2000) #related to degree, dont change
    servo.set_period(6, 19500)
    servo.set_acceleration(6, 2000)  # Slow acceleration
    servo.set_velocity(6, 10000)  # Full speed


    servo.set_position(0, 0) # 0 =Start position, Range -9000..9000
    servo.enable(0)
    print('servo0 start pos enabled')

    servo.set_position(3, 0)   #-11000 arm2 down, 0 arm2 up
    servo.enable(3)
    print('servo3 start pos enabled')

    servo12_pos = 4000
    servo.set_position(1, servo12_pos)
    servo.enable(1)
    #print(servo.get_position(1))

    #servo.set_position(2, -servo12_pos)
    #servo.enable(2)

    servo.set_position(5, 0) # 0 =Start position, Range 0..3000
    servo.enable(5)
    print('servo5 start pos enabled')

    servo.set_position(6, 0)
    servo.enable(6)
    print('servo6 start pos enabled')

    servo.disable(4) #rotate arm2 not activated

    #servo.disable(5)
    #servo.disable(6)
    #servo.disable(1)
    #servo.disable(2)
    #servo.disable(0)

    while True:
        # range -9000..9000
        if keyboard.is_pressed('q'):  # arm1, arm2 moving down
            servo.set_position(0, 0)
            servo.set_position(3, -8000)
            servo.set_position(1, servo12_pos)
            print('set arm1 pos')
            continue

        if keyboard.is_pressed('w'):  # gripper rotate
            servo.set_position(5, 1700)
            print('arm2  moving down')
            continue

        # gripper -10 000 geschlossen, 0 offen
        if keyboard.is_pressed('e'):  #final touch down
            servo.set_position(3, -9000)
            print('close grabber')
            continue

        if keyboard.is_pressed('r'):  # close gripper
            servo.set_position(6, -9000)
            continue

        if keyboard.is_pressed('t'):  # arm2  moving up
            servo.set_position(3, -9000)
            servo12_pos1 = 0
            servo.set_position(1, servo12_pos1)
            print('arm2  moving up')
            continue

        if keyboard.is_pressed('z'):  #-9000 front, 9000 wall
            servo.set_position(0, -9000)
            servo.set_position(6, -9000)
            print('arm1  rotate')
            continue

        if keyboard.is_pressed('u'):  # arm2  moving down
            servo.set_position(3, -10000)
            print('arm2  moving down')
            continue

            # gripper -10 000 geschlossen, 0 offen
        if keyboard.is_pressed('i'):  # close grabber
            servo.set_position(6, 0)
            print('open grabber')
            continue

        if keyboard.is_pressed('y'):  # reset start
            servo.set_position(0, 0)
            servo.set_position(3, 0)
            servo.set_position(5, 1500)
            servo.set_position(6, 0)
            continue

        if keyboard.is_pressed('x'):  # arm2  moving up
            servo.disable(0)
            servo.disable(1)
            servo.disable(2)
            servo.disable(3)
            servo.disable(4)
            servo.disable(5)
            servo.disable(6)
            print('all servos disabled')
            break

