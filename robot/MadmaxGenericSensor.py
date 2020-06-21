class GenericSensor:
    def __init__(self):
        pass

    def get_data(self):
        ''' should return dictionary sensor data'''
        raise NotImplementedError("Not implemented get_data() in child class")

    def get_interval(self):
        ''' should return seconds in float '''
        raise NotImplementedError("Not implemented get_interval() in child class")