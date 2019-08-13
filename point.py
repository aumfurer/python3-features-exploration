
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    p = Point(1, 2)
    print(sorted([p, 2*p, -1 * p]))
