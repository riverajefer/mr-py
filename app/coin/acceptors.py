from .. import SOCKET_IO, emit, APP
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
import threading


class CoinAcceptor():
    count = 0

    def __init__(self):
        self.count = 0
        self.pulse = 17

    def init(self):
        GPIO.setup(self.pulse, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('monederoo_ready!')
        SOCKET_IO.emit('monedero_ready')

    def start(self):
        self.init()
        with APP.app_context():
            x = threading.Thread(target=self.start_input)
            x.start()
        print('Start monedero!')

                
    def start_input(self):
        print('start_input!')
        while True:
            input_state = GPIO.input(self.pulse)
            if input_state == False:
                print('Boton Presionado')
                sleep(0.3)
                self.counter()
    
    def counter(self):
        self.count += 1;
        print('Counter: '+ str(self.count))
        with APP.test_request_context('/'):
            SOCKET_IO.emit('coin', {'coin': self.count*500 },  namespace='/')
