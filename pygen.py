from decimal import Decimal
from time import sleep


class PiGen:


    def __init__(self):
        self.k = Decimal(0.)
        self.p = Decimal(0.)
        self.tot = Decimal(0.)

        self.dec1 = Decimal(1.)
        self.teenth = Decimal(1./16.)
        self.dec8 = Decimal(8.)
        self.dec10 = Decimal(10.)


    def iter(self):
        pref = self.teenth**self.k

        f = lambda n, o: Decimal(n)/(self.dec8*self.k + Decimal(o))

        a = f(4, 1)
        b = f(2, 4)
        c = f(1, 5)
        d = f(1, 6)

        pwr = self.dec10**self.p

        self.tot += pref*(a-b-c-d)*pwr
        self.k += 1

        return self.tot


    def incp(self):
        self.tot -= Decimal(int(self.tot))
        self.tot *= self.dec10
        self.p += Decimal(1.)


    def current_digit(self):
        return int(self.tot)


    def get_next_digit(self):

        # set prev to negative number which will never appear in the sequence.
        prev_iteration = -1
        i = 0
        while self.current_digit() != prev_iteration:
            prev_iteration = self.current_digit()
            self.iter()
            i += 1

        rv = self.current_digit()

        self.incp()

        return rv
