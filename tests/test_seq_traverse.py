from functionali import (
    iter_,
    reversed_,
    first,
    ffirst,
    second,
    third,
    fourth,
    fifth,
    last,
    butlast,
    rest,
    take,
    drop,
    take_while,
    drop_while,
    split_with,
)

from typing import Iterator


def test_iter_():
    # tests that the behavior of iter_ differs from iter
    # When it comes to dictionaries
    d = {1: "a", 2: "b"}
    assert isinstance(iter_(d), Iterator) == True
    assert tuple(iter_({1: "a", 2: "b", 3: "c"})) == ((1, "a"), (2, "b"), (3, "c"))


def test_reversed_():
    d = {1: "a", 2: "b"}
    assert isinstance(reversed_(d), Iterator) == True
    assert tuple(reversed_({1: "a", 2: "b", 3: "c"})) == ((3, "c"), (2, "b"), (1, "a"))

    # test that iterators return a reversed iterators
    assert tuple(reversed_(iter([1, 2, 3]))) == (3, 2, 1)


def test_first():
    assert 1 == first([1, 2, 3])
    assert 1 == first((1, 2, 3))
    assert 1 == first({1, 2, 3})
    assert (1, "a") == first({1: "a", 2: "b"})
    assert None == first([])


def test_ffirst():
    assert 1 == ffirst([[1], [2], [3]])
    assert 1 == ffirst(((1,), (2,), (3,)))
    assert 1 == ffirst({(1, 2), (3, 4), (5, 6)})
    assert None == ffirst([])


def test_last():
    assert 3 == last([1, 2, 3])
    assert 3 == last((1, 2, 3))
    assert 3 == last({1, 2, 3})
    assert (3, "c") == last({1: "a", 2: "b", 3: "c"})
    assert None == last([])


def test_rest():
    # convert to tuple since rest returns iterator
    assert (2, 3) == tuple(rest([1, 2, 3]))
    assert (2, 3) == tuple(rest((1, 2, 3)))
    assert (2, 3) == tuple(rest({1, 2, 3}))
    assert ((2, "b"), (3, "c")) == tuple(rest({1: "a", 2: "b", 3: "c"}))
    assert () == tuple(rest([]))


def test_second():
    assert 2 == second([1, 2, 3])
    assert 2 == second(iter((1, 2, 3)))
    assert (2, "b") == second({1: "a", 2: "b"})
    assert None == second([])
    assert None == second([1])


def test_third():
    assert 3 == third([1, 2, 3])
    assert 3 == third(iter((1, 2, 3)))
    assert (3, "c") == third({1: "a", 2: "b", 3: "c"})
    assert None == third([])

    assert None == third([1, 2])


def test_fourth():
    assert 4 == fourth([1, 2, 3, 4])
    assert 4 == fourth(iter((1, 2, 3, 4)))
    assert 4 == fourth({1, 2, 3, 4})
    assert (4, "d") == fourth({1: "a", 2: "b", 3: "c", 4: "d"})
    assert None == fourth([])

    assert None == fourth([1, 2])


def test_fifth():
    assert 5 == fifth([1, 2, 3, 4, 5])
    assert 5 == fifth(iter((1, 2, 3, 4, 5)))
    assert 5 == fifth({1, 2, 3, 4, 5})
    assert (5, "e") == fifth({1: "a", 2: "b", 3: "c", 4: "d", 5: "e"})
    assert None == fifth([])

    assert None == fifth([1, 2])


def test_butlast():
    assert (1, 2) == butlast([1, 2, 3])
    assert (1, 2) == butlast(iter((1, 2, 3)))
    assert (1, 2) == butlast({1, 2, 3})
    assert ((1, "a"), (2, "b")) == butlast({1: "a", 2: "b", 3: "c"})
    assert None == butlast([1])
    assert None == butlast([])


def test_take():
    assert (1, 2, 3) == take(3, [1, 2, 3, 4, 5])
    assert () == take(3, [])
    assert ((1, "a"), (2, "b")) == take(2, {1: "a", 2: "b", 3: "c"})


def test_drop():
    assert (4, 5) == drop(3, [1, 2, 3, 4, 5])
    assert () == drop(3, [])
    assert ((3, "c"),) == drop(2, {1: "a", 2: "b", 3: "c"})


def test_take_while():
    def is_even(n):
        return n % 2 == 0

    def is_even_dict(d):
        # checks if the key of dict d is even
        return d[0] % 2 == 0

    assert (2, 4, 6) == take_while(is_even, [2, 4, 6, 7, 8, 9, 10])
    assert () == take_while(is_even, [1, 2, 4, 6, 7, 8, 9, 10])
    assert ((2, "a"), (4, "b")) == take_while(is_even_dict, {2: "a", 4: "b", 5: "c"})


def test_drop_while():
    def is_even(n):
        return n % 2 == 0

    def is_even_dict(d):
        # checks if the key of dict d is even
        return d[0] % 2 == 0

    assert (7, 8, 9, 10) == drop_while(is_even, [2, 4, 6, 7, 8, 9, 10])
    assert (1, 2, 4, 6, 7, 8, 9, 10) == drop_while(is_even, [1, 2, 4, 6, 7, 8, 9, 10])
    assert ((5, "c"),) == drop_while(is_even_dict, {2: "a", 4: "b", 5: "c"})


def test_split_with():
    def is_even(n):
        return n % 2 == 0

    assert ((2, 4, 6), (7, 8, 9, 10)) == split_with(is_even, [2, 4, 6, 7, 8, 9, 10])
    assert ((), (1, 2, 4, 6, 7, 8, 9, 10)) == split_with(
        is_even, [1, 2, 4, 6, 7, 8, 9, 10]
    )
