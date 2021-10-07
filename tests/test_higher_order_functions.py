from functionali import (
    curry,
    foldr,
    comp,
    flip,
    trampoline,
    count,
    is_even,
    threadf,
    threadl,
)

import pytest


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

    assert comp(count, filter)(is_even, [1, 2, 3, 4]) == 2


def test_curry():
    def fn(arg1, arg2, arg3):  # test function
        return [arg1, arg2, arg3]

    curried_fn = curry(fn)
    assert [1, 2, 3] == curried_fn(1)(2)(3)

    def fn_with_no_args():
        return 1

    curried_fn_with_no_args = curry(fn_with_no_args)
    assert 1 == curried_fn_with_no_args()


def test_flip():
    def fn(arg1, arg2, arg3):  # test function
        return [arg1, arg2, arg3]

    flipped_fn = flip(fn)

    assert [1, 2, 3] == fn(1, 2, 3)
    assert [1, 2, 3] != flipped_fn(1, 2, 3)
    assert [1, 2, 3] == flipped_fn(3, 2, 1)  # flipping args


def test_trampoline():
    def fact(x, curr=1, acc=1):
        if curr == x:
            return curr * acc
        else:
            return lambda: fact(x, curr + 1, acc * curr)

    assert trampoline(fact, 3) == 6


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, [lambda x: x]], 1),
        ([1, [[lambda a, b: a - b, 3]]], -2),
        ([1, [[lambda a, b: a + b, 2], [lambda a, b: a - b, 2]]], 1),
    ],
)
def test_threadf(input, expected):
    assert threadf(*input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, [lambda x: x]], 1),
        ([1, [[lambda a, b: a - b, 3]]], 2),
        ([1, [[lambda a, b: a + b, 2], [lambda a, b: a - b, 2]]], -1),
    ],
)
def test_threadf(input, expected):
    assert threadl(*input) == expected
