import threading
from time import sleep

class EventBus():
    def __init__(self):
        self.__threads = []
        self.__sensors = []

    def connect_sensor(self, sensor: object):
        sensor.set_callback(self.event_handler)
        self.__sensors.append(sensor)
        self.__create_tread(sensor)

    def __create_tread(self, sensor):
        thread = threading.Thread(target=sensor.run_stream)
        thread.start()
        self.__threads.append(thread)



    def event_handler(self, *args, **kwargs):
        print("Запущен ивент хендлер, тут будут обрабатыватся события от сенсоров")
        print(f"Аргументы переданные в функцию: {args}")
        pass
