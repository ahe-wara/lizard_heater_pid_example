import machine
import math
from machine import Pin

class PWM_Output:

        def __init__(self, pin, frequency, pwm_in_percentage):
            self.__pin = pin
            self.__frequency = frequency
            self.__pwm_in_percentage= pwm_in_percentage
            self.__pwm_output = machine.PWM(machine.Pin(self.__pin))
            self.__pwm_output.freq(self.__frequency)

        def __scale_duty_pwm(self, pwm_in_percentage):
            self.__duty_pwm = math.trunc(65535/100*pwm_in_percentage)   
            return self.__duty_pwm
            
        def set_pwm_outputfrequency(self, frequency):
            self.__pwm_output.freq(frequency)
        
        def run_pwm_output(self, pwm_in_percentage):
            self.__pwm_output.duty_u16(self.__scale_duty_pwm(pwm_in_percentage))
            print('Duty: %.2f' % (self.__pwm_output.duty_u16()))
            
        