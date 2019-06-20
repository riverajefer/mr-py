from .. import SOCKET_IO, emit, APP
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import threading

ITERA = 5
PULSE_INPUT = 17
FACTOR = 100

class CoinAcceptor():

    def __init__(self):
        self.pulse_input = 17
        self.pulses_counter = 0
        self.counter_control = 0        

    def init(self):
        GPIO.setup(PULSE_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('monederoo_ready!')
        SOCKET_IO.emit('monedero_ready')

    def start(self):
        self.init()
        x = threading.Thread(target=self.start_input)
        x.start()
        print('Start monedero!')
                
    def start_input(self):
        print('start_input!')
        while True:
            input_state = GPIO.input(PULSE_INPUT)
            if input_state == False:
                print('Boton Presionado')
                time.sleep(0.3)
                self.counter_control = 0
                self.pulses_counter += 1;
                print('count1 (): '+ str(self.pulses_counter))
            
            time.sleep(0.3)
            self.counter_control += 1;

            if (self.counter_control > 10) :  self.counter_control = 1
            
            print('counter_2: '+ str(self.counter_control))
            
            if(self.pulses_counter > 0 and self.counter_control > ITERA) : self.sendCounter()

    def sendCounter(self):
        print('COUNTER 1: '+ str(self.pulses_counter))
        SOCKET_IO.emit('coin', {'coin': (self.pulses_counter*FACTOR) },  namespace='/')
        self.pulses_counter = 0
        self.counter_control = 0 
    
    def stop(self):
        print('Stop monedero')