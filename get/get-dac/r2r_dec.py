import RPi.GPIO as GPIO
#import time

pins = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.182

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(pins, 0)

#def voltage_to_number(R2R):
#    if not (0.0 <= R2R <= dynamic_range):
#        print("напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
#        print("устанавливаем 0,0 В")
#        return 0
#    return int(R2R / dynamic_range * 255)

#def number_to_dac(num):
#    GPIO.output(pins, 0)
#    GPIO.output(pins, [int(el) for el in bin(num)[2:].zfill(8)])

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_voltage(self, num):
        GPIO.output(self, 0)
        GPIO.output(self, [int(el) for el in bin(num)[2:].zfill(8)])

    #def set_voltage(self, voltage):
    #    if not (0.0 <= voltage <= dynamic_range):
    #        print("напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
    #        print("устанавливаем 0,0 В")
    #        return 0
    #    return 0
    
if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], dynamic_range, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("вы ввели не числоб попробуйте ещё раз\n")

    finally:
        dac.deinit()