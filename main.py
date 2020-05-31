import threading

from robot.robot import MadmaxWheelbase, MadmaxSound
from time import sleep

from pydub import AudioSegment
from pydub.playback import play

wheels= MadmaxWheelbase()
sounds = MadmaxSound()

sounds.play_horn()
wheels.forward()

print(threading.active_count())
for i in range(10):
    sleep(0.3)
    wheels.set_speed(i/10)
    wheels.forward()

wheels.stop()


