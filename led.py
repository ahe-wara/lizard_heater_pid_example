from machine import Pin

class Led:

        def __init__(self, pin):
            self.__pin = pin
            self.__led = Pin(self.__pin, Pin.OUT)

        def on(self):
            self.__led.value(1)
        
        def off(self):
            self.__led.value(0)
            
        def toggle(self):          
            self.__led.toggle()