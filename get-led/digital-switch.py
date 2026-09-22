import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
button = 13
GPIO.setup(button, GPIO.OUT)
led_flag = 0
while True:
    if GPIO.input(button):
        led_flag = not led_flag
        GPIO.output(led, led_flag)
        time.sleep(0.2)
