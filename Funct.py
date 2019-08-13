from typing import Callable


class Adder:

    def __init__(self, base):
        self.base = base

    def __call__(self, x, y):
        return int(x, self.base)+int(y, self.base)


def adder2(base):
    def res(x, y):
        return int(x, base) + int(y, base)
    return res


def adder(x: str, y: str) -> int:
    return int(x)+int(y)


def main(f: Callable[[str, str], int]):
    print(f('10', '9'))


if __name__ == '__main__':
    print(adder2(15)('10', '9'))
