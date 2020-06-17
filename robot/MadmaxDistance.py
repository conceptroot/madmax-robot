import threading
from time import sleep
from robot.settings import sets
from gpiozero import DistanceSensor


class MadmaxDistance():
    def __init__(self):
        self._is_active= False
        self.distance_sensor = DistanceSensor(echo = sets['distance_echo'], trigger = sets['distance_trigger'])


    def _set_speed(self):
        while self._is_active:
            distance = self.distance_sensor.distance
            if (distance < 0.30):
                print("distance is less than 30cm, slow down")#ДОДЕЛАТЬ, ПОДУМАТЬ КАК можно установать значение в другом классе
                #так же подумать, что после увеличения безопасного растояния, не включать сразу полную скорость
                
            sleep(0.1)

    def run_distanse_speed_thread(self):
        self._is_active= True
        self._distanse_speed_thread = threading.Thread(target= self._set_speed)
        self._distanse_speed_thread.start()
    
    def stop_distanse_speed_thread(self):
        self._is_active = False