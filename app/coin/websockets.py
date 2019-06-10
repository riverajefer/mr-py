from .. import SOCKET_IO, emit
from .acceptors import CoinAcceptor
import random

list_coins = [50, 100, 200, 500, 1000]

coinAcceptor = CoinAcceptor()

@SOCKET_IO.on('connect')
def test_connect():
    print('conectado')
    emit('after connect',  {'data':'Lets dance www'})

@SOCKET_IO.on('start_monedero')
def coin_start():
    CoinAcceptor().start()

@SOCKET_IO.on('coin')
def coin():
    coin_rand =  random.choice(list_coins)
    emit('coin', {'coin': coin_rand })
    print('coin: '+str(coin_rand))