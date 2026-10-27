'''import RPi.GPIO as GPIO

dynamic_range = 3.182

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
pwm_obj = GPIO.PWM(12, 1000)
pwm_obj.start(0)

class PWM_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def number_to_dac(self, num):
        #bits = [int(el) for el in bin(num)[2:].zfill(8)]
        #GPIO.setup(12, GPIO.OUT)z`<`
        #pwm_obj = GPIO.PWM(12, 50)
        #pwm_obj.start(0)
        #num = (num/dynamic_range)
        if self.verbose:
            print(f"биты: {bits}")

    def voltage_to_number(self, num):
        if not (0.0 <= num <= dynamic_range):
            if self.verbose:
                print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
                print("устанавливаем 0,0 В")
            return 0
        return int(num / dynamic_range * 255)

    def set_voltage(self, voltage):
        #num = 
        #num = self.voltage_to_number(voltage)
        self.number_to_dac(num)
    
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, dynamic_range, True)

        while True:
            try:
                
                voltage = float(input("Введите напряжение в Вольтах: "))
                print(f"коэфицент заполнения: {round(voltage/dynamic_range*100, 2)}")
                dac.set_voltage(voltage)

            except ValueError:
                print("вы ввели не числоб попробуйте ещё раз\n")

    finally:
        dac.deinit()'''


import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        global pwm
        pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
        pwm.stop()
    def set_voltage(self, voltage):
        if not(0.0 <= voltage <= self.dynamic_range):
            print("bruh")
        else:
            nu = voltage/self.dynamic_range * 100
            print(nu)
            pwm.start(nu)


        return None
    
if __name__ == "__main__":
    try:
        d = 0
        dac = PWM_DAC(12, 500, 3.183, True)
        while True:
            try:
                voltage = float(input("Введите напряжене в Вольтах: "))
                dac.set_voltage(voltage)
                #pwm.ChangeDutyCycle(d)
                print("ok")
            except ValueError:
                print("Вы не ввели число. Попробуйте еще раз")
    finally:
        dac.deinit()