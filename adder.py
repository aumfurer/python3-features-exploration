from typing import Iterable, List, Any, TypeVar

from scipy.stats import zscore


T = TypeVar('T')


def double(xs: Iterable[T]) -> List[T]:
    return [x * 2 for x in xs]


def negative(xs):
    return [-x for x in xs]


def id_(xs):
    return xs


def sum_of_cubes(xs, pre_process=id_):
    xs = pre_process(xs)
    return sum(x ** 3 for x in xs)


def multiply_by(factor):
    def res(xs):
        return [x*factor for x in xs]
    return res


if __name__ == '__main__':
    print(sum_of_cubes(
        xs=range(5)
    ))
