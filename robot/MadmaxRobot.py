# Main class represents robot
from robot.settings import sets
from robot.MadmaxDistance import MadmaxDistance
from robot.MadmaxWheelbase import MadmaxWheelbase
from robot.MadmaxStepper import MadmaxStepper
from robot.MadmaxSound import MadmaxSound
from robot.MadmaxEventBus import EventBus


class MadmaxRobot(object):
    __ROBOT_MODES = ["auto", "bluetooth", "web"]
    __instance = None
    __threads = []
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            print("Creating MadmaxRobot object")
            cls.__instance = super(MadmaxRobot, cls).__new__(cls)
            return cls.__instance
        else:
            raise Warning("Warning!!! MadmaxRobot object already created")

            
    def __init__(self):
        # Create event bus for all sensors
        self.core_event_bus = EventBus()
        
        # Connect all components (hardware that conected to robot) 
        self.component_front_distance = MadmaxDistance() 
        self.component_wheel_base = MadmaxWheelbase()
        self.component_crusher_stepper = MadmaxStepper()
        self.component_sound = MadmaxSound()

        # Attach componets to event bus
        self.core_event_bus.connect_sensor(self.component_front_distance)

        # Set robot initial settings
        self.robot_mode = self.get_robot_mode(0) 
        self.robot_speed = sets['motors_speed']
        
    
    @staticmethod
    def get_robot_mode(number: int):
        try:
            return MadmaxRobot.__ROBOT_MODES[number]
        except IndexError:
            print(f"There is no robot mode number {number}\nSetting up mode 0")
            return MadmaxRobot.__ROBOT_MODES[0]

    def __create_thread(self):
        pass
    def __run_thread(self):
        pass

    def forward(self, speed = None):
        if speed:
            self.robot_speed = speed
        self.component_wheel_base.forward(speed)
    
    def stop(self):
        self.component_wheel_base.stop()
