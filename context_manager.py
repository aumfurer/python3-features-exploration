import time
from contextlib import contextmanager

class Timed:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.__initial = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{}: Took {}'.format(
            self.message,
            time.time() - self.__initial
        ))


@contextmanager
def timed(message):
    initial = time.time()
    yield
    print('{}: Took {}'.format(message, time.time() - initial))


def slow1(x):
    """
    :param x: i don't care
    :return:
    """
    time.sleep(0.2)
    return x


if __name__ == '__main__':

    with Timed('sarasa') as t:
        for xs in range(5):
            slow1(2)
