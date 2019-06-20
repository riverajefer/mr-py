from .. import SOCKET_IO
from .acceptors import CoinAcceptor

coinAcceptor = CoinAcceptor()

@SOCKET_IO.on('connect')
def test_connect():
    print('conectado')

@SOCKET_IO.on('start_monedero')
def coin_start():
    CoinAcceptor().start()

@SOCKET_IO.on('stop_monedero')
def coin():
    CoinAcceptor().stop()
