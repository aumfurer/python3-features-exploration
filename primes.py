from typing import Iterable


class RangoIterador:

    def __init__(self, r):
        self.c = 0
        self.r = r

    def __next__(self):
        if self.c >= self.r.upto:
            raise StopIteration
        else:
            r = self.c
            self.c += 1
            return r


class Rango:

    def __init__(self, upto):
        self.upto = upto

    def __iter__(self):
        return RangoIterador(self)


def rango_facil(upto):
    i = 0
    while i < upto:
        print('computing i:', i)
        yield i
        i += 1


def primes():
    prev = []
    i = 2
    while True:
        if not any(i % p == 0 for p in prev if p ** 2 <= i):
            prev.append(i)
            yield i
        i += 1


def double(xs):
    res = []
    for x in xs:
        res.append(x)
    return xs


if __name__ == '__main__':

   for p in primes():
       if p > 500:
           print(p)
           break