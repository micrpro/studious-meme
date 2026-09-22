import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
light = 6
GPIO.setup(light, GPIO.IN)
li = None
while (True):
    #GPIO.input(light)
    #print(GPIO.input(light))
    if(GPIO.input(light) == 0):
        GPIO.output(led, 1)
    else: 
        GPIO.output(led, 0)
    #time.sleep(0.2)