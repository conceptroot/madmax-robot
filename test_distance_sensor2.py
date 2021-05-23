from typing import List
import statistics
from time import sleep
from gpiozero import DistanceSensor
from statistics import median 
import colorama
from colorama import Fore
from rpi_lcd import LCD
from time import sleep
import redis
from datetime import date, datetime
import threading
import random


from robot.settings import sets

colorama.init(autoreset=True)
r = redis.Redis()

distance_sensor = DistanceSensor(echo = sets['distance_echo'], trigger = sets['distance_trigger'])
lcd = LCD(address=0x27, bus=1, width=16, rows=2)
KEY_RAW = 'distantion:raw:list'
KEY_MEDIAN = 'distantion:median:list'
KEY_MEAN= 'distantion:mean:list'
KEY_TIME = 'distantion:isotime'

for key in r.keys():
    r.delete(key)


def write_distance_raw_loop() -> None:
    while True:
        sleep(0.05)
        distance = round(distance_sensor.distance*100, 0)
        r.lpush(KEY_RAW, distance)
        r.ltrim(KEY_RAW, 0, 5000)
        r.set(KEY_TIME, datetime.now().isoformat())


def write_distance_clean_loop() -> None:
    while True:
        sleep(0.05)
        values = [float(v) for v in r.lrange(KEY_RAW, 0, 4)]
        try:
            mean = statistics.mean(values)
            median = statistics.median(values)
        except statistics.StatisticsError:
            continue
        r.set(KEY_MEDIAN, median)
        r.set(KEY_MEAN, mean)
        

def tread_informer() -> None:
    while True:
        sleep(0.3)

        try:
            iso_time = r.get(KEY_TIME).decode()
            time = datetime.fromisoformat(iso_time)
        except AttributeError:
            time = datetime(1970, 1,1) 

        mesures = r.llen(KEY_RAW)
        thread_len = r.llen('thread:list')
        keys = len(r.keys())
        lcd.text(f"{mesures}.Th={thread_len}.Ks={keys}", 1)

        median = r.get(KEY_MEDIAN)
        mean = r.get(KEY_MEAN)
        median = float(median) if median else -1.0
        mean = float(mean) if mean else -1.0

        lcd.text(f"av={mean:.0f} med={median:.0f}", 2)
        print(f"av={mean:.0f} med={median:.0f} mesures={mesures} threads={thread_len} time={time.strftime('%H:%M:%S')}")

thread_list: List[threading.Thread] = []
thread_list.append(threading.Thread(target=write_distance_raw_loop, name='Записыватель расстояний'))
thread_list.append(threading.Thread(target=tread_informer, name="Выводильщик растояний"))
thread_list.append(threading.Thread(target=write_distance_clean_loop, name="Записыватель чистых растояний"))


for thread in thread_list:
    r.rpush('thread:list', thread.getName())
    thread.start()

        

# for nice_dist in nice_distance(distance_sensor.distance):
#     lcd.text('Distance:', 1)
#     lcd.text(f'{nice_dist:.2f}', 2)
#     print(Fore.RED + f"distance = {nice_dist:.2f}")


lcd.clear()