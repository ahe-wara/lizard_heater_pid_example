from poti import Poti
from thermistor import Thermistor
from pwm_output import PWM_Output
from pid_controller import PID_Controller
from toggle_button_event_handler import Toggle_Button_Event_Handler
from led import Led
from data_logger import Data_Logger
from usb_connection import Usb_Connection
import time

set_temperature = 32.0
sample_time_ms = 1000
pid_controller_on = True

poti = Poti(27)
led = Led(15)
thermistor = Thermistor(28)
pwm_output = PWM_Output(0,10,0)
pid_controller = PID_Controller(sample_time_ms, 100.0, 0.0, 20, 0.0001, 0.5)
button_event_handler = Toggle_Button_Event_Handler(14, pid_controller_on)
usb_connection = Usb_Connection()
#optional_data_logger 
#data_logger = Data_Logger("test.txt")

while True:
    pid_controller_on = button_event_handler.get_state()
    if pid_controller_on: 
        led.on()
        pwm_output.run_pwm_output(pid_controller.run(set_temperature ,thermistor.temperature()))
        #print('PID Controller PWM output in perc.: %.2f' % (pid_controller.run(set_temperature, thermistor.temperature())))
        #print('Set Temperature in °C: %.2f' % (set_temperature))
        #print('Actual Temperature in °C: %.2f' % (thermistor.temperature()))
    elif not pid_controller_on:
        led.off()
        pwm_output.run_pwm_output(poti.poti_state_in_percentage())
        #print('Poti state in perc.: %.2f' % (poti.poti_state_in_percentage()))
        #print('Actual Temperature in °C: %.2f' % (thermistor.temperature()))
    
    #data_logger.write_to_logger(usb_connection.read())
    #data_logger.write_to_logger(str(thermistor.temperature()))
    #usb_connection.write(thermistor.temperature())

    time.sleep_ms(sample_time_ms)
