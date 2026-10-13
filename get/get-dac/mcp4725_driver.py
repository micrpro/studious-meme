import smbus
#import RPi.GPIO as GPIO

dynamic_renge = 5.12

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_renge = verbose
        self.dynamic_renge = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("на выход ЦАП можно подовать только целые числа")

        if not(0 <= number <= 4095):
            print("число выходит за разрядность MCP4752")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
        num = int(voltage/self.dynamic_renge * 4095)
        self.set_number(num)
    
if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_renge)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("вы ввели не числоб попробуйте ещё раз\n")

    finally:
        dac.deinit()