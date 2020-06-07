# Modules:
1. Motors (chassis)
2. Sounds 
3. Led Pixels (headlights)
4. Stepper motor (crusher lifting gear)
5. Infrared Obstacle Avoidance Sensor 
## 1. Motors
**Library:**
gpiozero

**Hardware:**
l298n - driver.

## 2. Sounds
**Library:**
pydub

https://realpython.com/playing-and-recording-sound-python/

## 3. Led Pixels
**Libraries:**
rpi_ws281x, adafruit-circuitpython-neopixel

**Hardware**
[WS2812B led strip](https://aliexpress.ru/item/32958709980.html?spm=a2g0s.9042311.0.0.264d33edLvvHx5)

**TODO**
1. Right now to run Pixels you should run the script with sudo preveiges. Fix this issue

## 4. Stepper motor (crusher lifting gear)
**Libraries:**
RPi.GPIO

**Hardware:**
[motor 28BYJ-48-12V](https://aliexpress.ru/item/4000040714477.html?spm=a2g0o.productlist.0.0.6bfa5a106acnOu&algo_pvid=78c7cbc5-8e20-48c3-a600-54b9dd9b3f6d&algo_expid=78c7cbc5-8e20-48c3-a600-54b9dd9b3f6d-56&btsid=0ab50f6115910435359073048ef66c&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)
+ 
[A3967 EasyDriver](https://aliexpress.ru/item/32831233631.html?spm=a2g0o.productlist.0.0.41f94ed4nbO92k&algo_pvid=9e0c55d1-31fb-4f5e-bc1a-6a04935f2690&algo_expid=9e0c55d1-31fb-4f5e-bc1a-6a04935f2690-0&btsid=0ab50f6115910436801802540ef66c&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)

**TODO**
1. find library

## 5. Infrared Obstacle Avoidance Sensor 
**Libraries:**
RPi.GPIO

**Hardware:**
[IR Obstacle Avoidance Sensor. LM393](https://www.aliexpress.com/item/32462888575.html?spm=a2g0o.productlist.0.0.10505e792u3bFR&algo_pvid=7a6e7ce7-10a9-4930-b219-f44ed0643d0d&algo_expid=7a6e7ce7-10a9-4930-b219-f44ed0643d0d-0&btsid=0b8b037015915452825724033edd4b&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)

**TODO**
1. Add information about voltage divider. (voltage divider is necessary, beacouse IR sensor don't enough 3.3 volts or use logic shifter)
2. 