from machine import Pin

class Button_Event_Handler:


        
    def __init__(self, pin):
        print ('Init')
        self.__pin = pin
        self.__button = Pin(self.__pin, Pin.IN, Pin.PULL_DOWN)
        self.__button.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = self.__button_handler)
        
    def __button_handler(self, Pin):
        if self.__button.value():
           print("Button gedrückt")
        elif not self.__button.value():
           print("Button nicht gedrückt")