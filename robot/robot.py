from gpiozero import Robot
import threading
from robot.settings import sets

class MadmaxWheelbase():
    def __init__(self):
        self.wheel_base = Robot(
            left=(sets['motor_in1_left'],sets['motor_in2_left'],sets['motor_enabler_left']), 
            right=(sets['motor_in3_right'],sets['motor_in4_right'],sets['motor_enabler_right']))
        self.speed = 0.3
    def forward(self, speed = None):
        if speed: 
            self.speed = speed
        self.wheel_base.forward(self.speed)
    def backward(self, speed = None):
        if speed: 
            self.speed = speed
        self.wheel_base.backward(self.speed)   
    def stop(self):
        self.wheel_base.stop()
    def set_speed(self, speed):
        self.speed = speed 



class MadmaxPixels():
    def __init__(self):
        pass