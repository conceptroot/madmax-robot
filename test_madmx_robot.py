from time import sleep
from robot.MadmaxRobot import MadmaxRobot


robot = MadmaxRobot()
robot.component_sound.play_horn()
sleep(2)
robot.forward()

sleep(1)
robot.stop()