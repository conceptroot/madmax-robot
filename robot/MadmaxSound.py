import threading
from pydub import AudioSegment
from pydub.playback import play

class MadmaxSound():
    def __init__(self):
        self._horn_sound = AudioSegment.from_mp3('robot/sounds/horn.mp3')
    def _play_horn(self):
        play(self._horn_sound)
    def play_horn(self):
        thread = threading.Thread(target = self._play_horn)
        thread.start()