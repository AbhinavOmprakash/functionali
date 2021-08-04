from functionali import (
    curry,
    foldr,
    comp,
    flip,
)


def test_foldr():
    sub = lambda e, acc: acc - e  # foldr function
    assert foldr(sub, [1, 2, 3, 10]) == 4  # (((10-3)-2)-1) = 4
    assert foldr(sub, [1, 2], 10) == 7  # ((10-2)-1) == 7
    assert foldr(sub, iter([1, 2, 3, 10])) == 4  # (((10-3)-2)-1) = 4


def test_compose():
    inc = lambda x: x + 1
    double_it = lambda x: x * 2

    assert comp(inc, double_it)(5) == inc(
        double_it(5)
    )  # inc(double_it(5)) => inc(10) => 11
    assert comp(double_it, inc)(5) == 12  # double_it(inc(5)) => double_it(6) => 12


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
