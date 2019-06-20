from .. import SOCKET_IO
from .acceptors import BillAcceptor

billAcceptor = BillAcceptor()

@SOCKET_IO.on('connect')
def test_connect():
    print('conectado')

@SOCKET_IO.on('start_bill')
def coin_start():
    pass
    # billAcceptor().start()

@SOCKET_IO.on('stop_bill')
def coin():
    pass
    #billAcceptor().stop()
