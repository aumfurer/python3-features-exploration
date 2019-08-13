import time


def slow_sum(a, b):
    print(".", end='', flush=True)
    time.sleep(1)
    return a + b


class AccumulatedSlow:

    def __init__(self, xs):
        self.xs = xs
        self.acc = 0
        self.index = 0

    def __iter__(self):
        self.acc = 0
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.xs):
            raise StopIteration()
        self.acc = slow_sum(self.acc, self.xs[self.index])
        self.index += 1
        return self.acc


def accumulated_slow(xs):
    res = []
    acc = 0
    for x in xs:
        acc = slow_sum(acc, x)
        res.append(acc)
    return res


# Find first j=slow(i) such j**2 > 33


if __name__ == '__main__':
    print("start")
    for i, acc in enumerate(AccumulatedSlow(range(10))):
        if acc > 5:
            print('\n', i)
            break
    print("\nend")
