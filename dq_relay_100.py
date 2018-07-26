import sys
import time
from raspihats.i2c_hats import DQ10rly

boards = [
    DQ10rly(0x50), 
    DQ10rly(0x51), 
    DQ10rly(0x52), 
    DQ10rly(0x53), 
    DQ10rly(0x54),
    DQ10rly(0x55),
    DQ10rly(0x56),
    DQ10rly(0x57),
    DQ10rly(0x58),
    DQ10rly(0x59)
]

def set_dq_value(boards, value):
    for b in boards:
        b.dq.value = value

def main():

    print("Use 'Ctrl + C' to stop")

    try:
        set_dq_value(boards, 0)

        while True:
            for b in boards:
                for i in range(0, 10):
                    b.dq.channels[i] = True
                    time.sleep(0.02)
                    b.dq.channels[i] = False

            for i in range(0, len(boards)):
                set_dq_value(boards, 0x3FF)
                time.sleep(0.5)
                
                set_dq_value(boards, 0)
                time.sleep(0.5)

    except KeyboardInterrupt:
        pass

    finally:
        set_dq_value(boards, 0)


if __name__ == "__main__":
    main()
