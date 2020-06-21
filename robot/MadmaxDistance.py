from time import sleep
from gpiozero import DistanceSensor

from robot.settings import sets
from robot.MadmaxGenericSensor import GenericSensor

class MadmaxDistance(GenericSensor):
    def __init__(self):
        super().__init__()
        self._distance_sensor = DistanceSensor(echo = sets['distance_echo'], trigger = sets['distance_trigger'])
        self._interval = 0.5

    def _get_data(self):
        distance = self._distance_sensor.distance
        return distance