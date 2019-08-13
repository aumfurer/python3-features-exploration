
class Square:

    def __init__(self, width):
        self.__width = width

    @property
    def area(self):
        return self.__width**2

    @area.setter
    def area(self, area):
        self.__width = area**.5


if __name__ == '__main__':
    s = Square(2)
    s.area = 2
    print(dir(s))
