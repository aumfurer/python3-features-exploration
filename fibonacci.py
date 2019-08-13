import time
import pickle
import os
from functools import wraps


def pickled(filename: str):
    def decorator(f):
        def wrapped(x):
            file = filename.format(x) +'.pickle'
            if os.path.exists(file):
                with open(file, 'rb') as fi:
                    return pickle.load(fi)
            else:
                res = f(x)
                with open(file, 'wb') as fi:
                    pickle.dump(res, fi)
                return res
        return wrapped
    return decorator


def cached(f):
    cache = {}

    @wraps(f)
    def decorated(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return decorated


def timed(msg="time elapsed ="):
    def timed_res(f):
        @wraps(f)
        def wrapper(x):
            """sarasa"""
            t = time.time()
            res = f(x)
            print(msg, time.time() - t)
            return res

        return wrapper

    return timed_res


@cached
def fibo(x):
    if x < 2:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)


@timed("slow1 takes")
def slow1(x):
    """
    :param x: i don't care
    :return:
    """
    time.sleep(2)
    return x


@timed("slow2 takes")
def slow2(x):
    time.sleep(1)
    return x


@timed("predict_random_forest takes")
def predict_random_forest(xs):
    time.sleep(3)


def suma(*args, **kwargs):
    print(kwargs)
    print(args)
    return sum(args)


@pickled('fibo{}')
@timed()
def fibo_aux(x):
    print("calculando")
    return fibo(x)


if __name__ == '__main__':
    print(fibo_aux(6))

