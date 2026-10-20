import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.182
signal_frequency = 10
sampling_frequency = 1000
x=1

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], amplitude, True)

    while True:
        t = time.time()
        #print(x)
        voltage = sg.get_sin_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        #print("2")
        sg.wait_for_sampling_period(sampling_frequency)
        #print("3")

finally:
    dac.deinit()