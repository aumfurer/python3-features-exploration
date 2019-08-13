from typing_extensions import Protocol

from not_my_code import *


class Duck(Protocol):
    def quack(self):
        raise NotImplementedError()

    def fly(self):
        raise NotImplementedError()


class EnglishDuck:
    def quack(self):
        print("Quack Quack!")

    def fly(self):
        print("I'm flying")


class SpanishDuck:
    def quack(self):
        print("¡Cuac Cuac!")

    def fly(self):
        print("Estoy volando")


class Eagle:
    def fly(self):
        print("I'm flying")


def see_a_duck(d: Duck):
    d.fly()
    d.quack()


if __name__ == '__main__':
    see_a_duck(ChineseDuck())

