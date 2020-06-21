import threading
from time import sleep

class EventBus():
    def __init__(self):
        self.__threads = []
        self.__sensors = []

        
    def connect_sensor(self, sensor: object):
        # sensor.get_data()
        pass

    def create_tread(self):
        pass

    def run_callback(self, callback_function, *args, **kwargs):
        callback_function(*args, **kwargs)