import RPi.GPIO as GPIO
#import time

pins = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.182

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(pins, 0)

def voltage_to_number(R2R):
    if not (0.0 <= R2R <= dynamic_range):
        print("напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("устанавливаем 0,0 В")
        return 0
    return int(R2R / dynamic_range * 255)

def number_to_dac(num):
    GPIO.output(pins, 0)
    GPIO.output(pins, [int(el) for el in bin(num)[2:].zfill(8)])
try:
    while True:
        try:
            voltage = float(input("введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
                print("Вы ыыели число, Попробуйте ещё раз\n")

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()