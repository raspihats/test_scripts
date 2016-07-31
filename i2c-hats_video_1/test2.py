from raspihats.i2c_hats import Rly10
from time import sleep

board1 = Rly10(0x50)
board2 = Rly10(0x51)

for i in range(0, 10):
    board1.do_set_state(i, True)
    sleep(0.5)
    board1.do_set_state(i, False)

for i in range(0, 10):
    board2.do_set_state(i, True)
    sleep(0.5)
    board2.do_set_state(i, False)
