from .. import SOCKET_IO, emit

class CoinAcceptor():

    def init(self):
        print('monederoo_ready!')
        SOCKET_IO.emit('monedero_ready')

    def start(self):
        print('Start monedero!')
