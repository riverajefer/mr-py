from .. import SOCKET_IO, emit
import RPi.GPIO as gpio
from time import sleep
class CoinAcceptor():

    __INPUT_PULSE = 23
    count = 0

    def __init__(self):
        self.count = 0

    def init(self):
        gpio.setup(__INPUT_PULSE,gpio.IN,pull_up_down=gpio.PUD_UP)
        print('monederoo_ready!')
        SOCKET_IO.emit('monedero_ready')

    def start(self):
        print('Start monedero!')

    def check_inputs(self):
        input_state=gpio.input(__INPUT_PULSE)
        if input_state==False:
            print('Boton Presionado')
            sleep(0.3)      # si no lo es la apaga
            self.counter()
        else:
            gpio.output(__INPUT_PULSE,0) 
    
    def counter(self):
        ''' 
        global contador
        contador += 1 
        '''
        self.count +=1 
        print('count: '+ str(count))
