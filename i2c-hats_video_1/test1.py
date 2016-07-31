from raspihats.i2c_hats import Rly10
from time import sleep

board = Rly10(0x50)

for i in range(0, 10):
    board.do_set_state(i, True)
    sleep(0.5)
    board.do_set_state(i, False)