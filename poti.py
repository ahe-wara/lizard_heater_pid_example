import machine
import math
from machine import Pin

class Poti:

        def __init__(self, pin):
            self.__pin = pin
            self.__poti_state_in_percentage = 0.0
            self.__poti = machine.ADC(self.__pin)

        def poti_state_in_percentage(self):
            self.__poti_state_in_percentage = 100/65535*self.__poti.read_u16()
            return self.__poti_state_in_percentage
