from time import sleep
from robot.MadmaxRobot import MadmaxRobot

from robot.MadmaxGenericSensor import GenericSensor

robot = MadmaxRobot()
# robot.component_sound.play_horn()

sleep(2)
print("forward")
robot.forward()

sleep(1)
print("stop")
robot.stop()
