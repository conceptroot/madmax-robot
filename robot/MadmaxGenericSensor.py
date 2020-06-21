from time import sleep
class GenericSensor:
    def __init__(self):
        self._callback_function = None
        self._is_active = True
        self._interval = 1

    def run_stream(self):
        ''' should return dictionary sensor data'''
        while self._is_active:
            self._callback_function(self._get_data())
            sleep(self._interval)

    def _get_data(self):
        '''should return dictionary with sensor data'''
        raise NotImplementedError("Not implemented _get_data() in child class")

    def get_interval(self):
        ''' should return seconds in float '''
        raise NotImplementedError("Not implemented get_interval() in child class")
    
    def set_callback(self, callback_function):
        self._callback_function = callback_function
        