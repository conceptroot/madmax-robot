import threading

from robot.robot import MadmaxWheelbase, MadmaxSound
from robot.MadmaxStepper import MadmaxStepper
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
LEFT = 23
RIGHT = 24
GPIO.setup([LEFT, RIGHT], GPIO.IN)



while True:
    print("LEFT = ", GPIO.input(LEFT))
    print("RIGHT = ", GPIO.input(RIGHT))
    sleep(1)