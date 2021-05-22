import threading

import colorama

from robot.MadmaxWheelbase import MadmaxWheelbase 
from robot.MadmaxStepper import MadmaxStepper
from robot.MadmaxSound import MadmaxSound
from time import sleep

colorama.init(autoreset=True)


print(colorama.Fore.YELLOW + "initialising... Wheels")
wheels= MadmaxWheelbase()
print(colorama.Fore.BLUE + "initialising... Sound")
sounds = MadmaxSound()
print(colorama.Fore.GREEN + "initialising... Stepper")
stepper_crusher = MadmaxStepper()



def main():
    sounds.play_horn()

    print(colorama.Fore.RED + "Printing active thread count")
    print(colorama.Fore.RED + str(threading.active_count()))

    for i in range(10):
        sleep(0.3)
        wheels.set_speed(i/10)
        wheels.forward()
    wheels.stop()

    stepper_crusher.rotate(360, True)


try:
    main()
except KeyboardInterrupt:
    print(colorama.Fore.GREEN + "Stop motors\nGood buy!")
    wheels.stop()