from functionali import (
    curry,
    foldr,
    flip,
)

from operator import add, sub, mult

def test_foldr():
    assert foldr(sub, [1, 2, 3, 10]) == 4  # (((10-3)-2)-1) = 4
    assert foldr(sub, iter([1, 2, 3, 10])) == 4  # (((10-3)-2)-1) = 4

def test_compose():
    


def test_curry():
    def fn(arg1, arg2, arg3):  # test function
        return [arg1, arg2, arg3]

    curried_fn = curry(fn)
    assert [1, 2, 3] == curried_fn(1)(2)(3)


def test_flip():
    def fn(arg1, arg2, arg3):  # test function
        return [arg1, arg2, arg3]

    flipped_fn = flip(fn)

    assert [1, 2, 3] == fn(1, 2, 3)
    assert [1, 2, 3] != flipped_fn(1, 2, 3)
    assert [1, 2, 3] == flipped_fn(3, 2, 1)  # flipping args
