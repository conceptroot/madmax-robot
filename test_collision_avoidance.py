import threading

from robot.robot import *
from robot.MadmaxStepper import MadmaxStepper
from robot.MadmaxWheelbase import MadmaxWheelbase
from robot.MadmaxSound import MadmaxSound
from robot.MadmaxDistance import MadmaxDistance
from time import sleep

wheels= MadmaxWheelbase()
sounds = MadmaxSound()

# sounds.play_horn()

# wheels.forward()

# print(threading.active_count())
# for i in range(10):
#     sleep(0.3)
#     wheels.set_speed(i/10)
#     wheels.forward()

# wheels.stop()


# stepper_crusher = MadmaxStepper()
# stepper_crusher.rotate(360, True)


import RPi.GPIO as GPIO
LEFT = 24
RIGHT = 23
GPIO.setup([LEFT, RIGHT], GPIO.IN)

def print_GPIO():
    while True:
        print("LEFT = ", GPIO.input(LEFT))
        print("RIGHT = ", GPIO.input(RIGHT))
        sleep(1)
# print_GPIO()

# thread_GPIO = threading.Thread(target = print_GPIO)
# thread_GPIO.start()


# sence = MadmaxDistance()
# sence.run_distanse_speed_thread()

try:
    while True:
        # print_GPIO()
        if GPIO.input(RIGHT) and GPIO.input(LEFT):
            wheels.forward(0.2)
        else:
            wheels.stop()
        sleep (0.2)
except KeyboardInterrupt:
    print("zavershaem")
    wheels.stop()