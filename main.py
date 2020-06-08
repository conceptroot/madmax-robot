import threading

from robot.MadmaxWheelbase import MadmaxWheelbase 
from robot.MadmaxStepper import MadmaxStepper
from robot.MadmaxSound import MadmaxSound
from time import sleep

wheels= MadmaxWheelbase()
sounds = MadmaxSound()

sounds.play_horn()
wheels.forward()
stepper_crusher = MadmaxStepper()



print(threading.active_count())
for i in range(10):
    sleep(0.3)
    wheels.set_speed(i/10)
    wheels.forward()

wheels.stop()


stepper_crusher.rotate(360, True)