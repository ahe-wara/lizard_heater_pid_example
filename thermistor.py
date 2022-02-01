import machine
import math
from machine import Pin

class Thermistor:

        def __init__(self, pin):
            self.__pin = pin
            self.__temp_in_C = 0
            self.__thermistor = machine.ADC(self.__pin)

        def temperature(self):          
            temperature_value = self.__thermistor.read_u16()
            Vr = 3.3 * float(temperature_value) / 65535
            Rt = 10000 * Vr / (3.3 - Vr)
            temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
            self.__temp_in_C = temp - 273.15
            #Fah = Cel * 1.8 + 32
            #measure_time = math.trunc((time.ticks_diff(time.ticks_ms(),start_time))/1000)
            #print ('%.1f ; %.2f C' % (measure_time, Cel))
            return self.__temp_in_C

        