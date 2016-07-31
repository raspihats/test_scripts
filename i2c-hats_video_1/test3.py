from raspihats.i2c_hats import Rly10, Di16
from time import sleep

board1 = Rly10(0x50)
board2 = Rly10(0x51)
board3 = Di16(0x40)

while True:
    state = board3.di_get_state(0)    # can use label 'Di1.1' instead of index 0
    board1.do_set_state(0, state)     # can use label 'Rly1' instead of index 0
    board2.do_set_state(1, state)     # can use label 'Rly2' instead of index 1
    sleep(0.03)
