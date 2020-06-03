from robot.settings import sets
import RPi.GPIO as GPIO
import threading
from time import sleep

class MadmaxStepper(object):
    def __init__(self, 
            enable_pin= sets['stepper_enable_pin'], 
            step_pin= sets['stepper_step_pin'], 
            direction_pin= sets['stepper_direction_pin'], 
            revolution_steps= sets['stepper_revolution_steps'],
            microsteps_in_one_step = sets['stepper_microsteps_in_one_step']):
        self._revolution_steps = revolution_steps
        self._microsteps_in_one_step = microsteps_in_one_step
        self._step_pin = step_pin
        self._dir_pin = direction_pin
        self._en_pin = enable_pin
        self._init_GPIO()

    def _init_GPIO(self):
        GPIO.setup(self._pins, GPIO.OUT) 
        GPIO.output(self._en_pin, GPIO.LOW)
    
    @property
    def _pins(self):
        return [self._en_pin, self._step_pin, self._dir_pin] 

    def _get_steps_by_angle(self, angle):
        steps_by_angle = (self._revolution_steps*angle*self._microsteps_in_one_step)//360
        print("steps_by_angle = ", steps_by_angle)
        return steps_by_angle        

    def rotate(self, angle, is_cw=True):
        print("starting rotate function in MadmaxStepper")
        GPIO.output(self._en_pin, GPIO.LOW)
        GPIO.output(self._dir_pin, is_cw)
        for _ in range(self._get_steps_by_angle(angle)):
            GPIO.output(self._step_pin, GPIO.HIGH)
            sleep(0.0003)
            GPIO.output(self._step_pin, GPIO.LOW)
            sleep(0.0003)
            
        GPIO.output(self._en_pin, GPIO.HIGH)