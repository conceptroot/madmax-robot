from rpi_lcd import LCD
from time import sleep

lcd = LCD(address=0x27, bus=1, width=16, rows=2)

lcd.text('Hello World!', 1)
lcd.text('Raspberry Pi', 2)

sleep(2)
lcd.clear()

lcd.text("This is test string for i2c lcd screen, which has 16x2 demension.", 1)
sleep(5)