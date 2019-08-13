from typing import Optional


class Tree:

    def __init__(self, l: Optional['Tree'], v, r: Optional['Tree']):
        self.l = l
        self.v = v
        self.r = r

    def __str__(self):
        return "({}, {}, {})".format(
            self.l if self.l else 'Nil',
            self.v,
            self.r if self.r else 'Nil'
        )

    def __iter__(self):
        def res():
            if self.l:
                yield from self.l
            yield self.v
            if self.r:
                yield from self.r
        return res()


if __name__ == '__main__':
    r"""
             1
            / \
           2   5
         /  \
        3    4
    """
    t = Tree(Tree(Tree(None, 3, None), 2, Tree(None, 4, None)), 1, Tree(None, 5, None))
    for x in t:
        print(x)
