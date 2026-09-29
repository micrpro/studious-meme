import RPi.GPIO as GPIO
import time

leds = [16, 12, 25, 17, 27, 23, 22, 24]
bu_down = 10
bu_up = 9
num = 0
sleep_time = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, 0)
GPIO.setup(bu_up, GPIO.IN)
GPIO.setup(bu_down, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    if GPIO.input(bu_up):
        if (num <= 255):
            num = num + 1
            #print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
    if GPIO.input(bu_down) :
        if(num >= 2):
            num = num - 1
            #print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)