from machine import Pin

class Toggle_Button_Event_Handler:
       
    def __init__(self, pin, on_off):
        self.__pin = pin
        self.__on_off = on_off
        self.__button = Pin(self.__pin, Pin.IN, Pin.PULL_DOWN)
        self.__button.irq(trigger = Pin.IRQ_RISING, handler = self.__button_handler)   # |Pin.IRQ_FALLING for both

        
    def __button_handler(self, Pin):
        self.__set_state()
    
    def get_state(self):
        return self.__on_off
    
    def __set_state (self):
        if not self.__on_off:
           self.__on_off = True
        elif self.__on_off:
           self.__on_off = False