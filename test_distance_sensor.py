from time import sleep
from gpiozero import DistanceSensor
from statistics import median 
import colorama
from colorama import Fore

from robot.settings import sets

colorama.init(autoreset=True)

distance_sensor = DistanceSensor(echo = sets['distance_echo'], trigger = sets['distance_trigger'])

def nice_distance(distanse: float) -> float:
    SLEEP_TIME = 0.1
    mesure_list_5 = []
    while True:
        # что-то перемудрил
        for _ in range(5):
            dist = distance_sensor.distance
            # print(f"{dist}")
            if isinstance(dist, float):
                mesure_list_5.append(dist)
                # print(dist)
            while len(mesure_list_5) > 5:
                mesure_list_5.pop(0)
            sleep(SLEEP_TIME/6)
        yield median(mesure_list_5)
        sleep(SLEEP_TIME/6)
        

# while True:
    # print(f"distance = {distance_sensor.distance}")
for nice_dist in nice_distance(distance_sensor.distance):
    print(Fore.RED + f"distance = {nice_dist:.2f}")