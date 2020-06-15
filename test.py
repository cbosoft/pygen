import sys

from pygen import PiGen
from digits_of_pi import DIGITS_OF_PI


def fail(i, digit_exp, digit_got):
    print(f'Test failed at digit #{i} (expected {digit_exp}, got {digit_got})')
    sys.exit(1)


def test():
    pg = PiGen()

    for i, digit in enumerate(DIGITS_OF_PI):
        digit_got = pg.get_next_digit()
        print(digit, digit_got)
        if digit != digit_got:
            fail(i, digit, digit_got)


if __name__ == '__main__':
    test()
