from thermistor import Thermistor
from pwm_output import PWM_Output
from pid_controller import PID_Controller
from button_event_handler import Button_Event_Handler
import time

set_temperature = 32.0
sample_time_ms = 1000

thermistor = Thermistor(28)
pwm_output = PWM_Output(0,10,0)
pid_controller = PID_Controller(sample_time_ms, 100, 0, 20, 0.0001, 0.5)
button_event_handler = Button_Event_Handler(14)

while True:
    pwm_output.run_pwm_output(pid_controller.run(set_temperature ,thermistor.temperature()))
    print('PID Controller PWM output in perc.: %.2f' % (pid_controller.run(32.0,thermistor.temperature())))
    print('Set Temperature in °C: %.2f' % (set_temperature))
    print('Actual Temperature in °C: %.2f' % (thermistor.temperature()))
    time.sleep_ms(sample_time_ms)

    
    