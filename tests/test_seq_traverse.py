from functionali import (
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
    assert 2 == second((1, 2, 3))
    assert 2 == second({1, 2, 3})
    assert (2, "b") == second({1: "a", 2: "b"})
    assert None == second([])
    # check that the last item is returned
    # when iterable is shorter than two
    assert 1 == second([1])


def test_third():
    assert 3 == third([1, 2, 3])
    assert 3 == third((1, 2, 3))
    assert 3 == third({1, 2, 3})
    assert (3, "c") == third({1: "a", 2: "b", 3: "c"})
    assert None == third([])
    # check that the last item is returned
    # when iterable is shorter than Three
    assert 2 == third([1, 2])


def test_fourth():
    assert 4 == fourth([1, 2, 3, 4])
    assert 4 == fourth((1, 2, 3, 4))
    assert 4 == fourth({1, 2, 3, 4})
    assert (4, "d") == fourth({1: "a", 2: "b", 3: "c", 4: "d"})
    assert None == fourth([])
    # check that the last item is returned
    # when iterable is shorter than Four
    assert 2 == fourth([1, 2])
    assert 3 == fourth([1, 2, 3])


def test_fifth():
    assert 5 == fifth([1, 2, 3, 4, 5])
    assert 5 == fifth((1, 2, 3, 4, 5))
    assert 5 == fifth({1, 2, 3, 4, 5})
    assert (5, "e") == fifth({1: "a", 2: "b", 3: "c", 4: "d", 5: "e"})
    assert None == fifth([])
    # check that the last item is returned
    # when iterable is shorter than five
    assert 2 == fifth([1, 2])
    assert 3 == fifth([1, 2, 3])
    assert 4 == fifth([1, 2, 3, 4])


def test_butlast():
    assert (1, 2) == butlast([1, 2, 3])
    assert (1, 2) == butlast((1, 2, 3))
    assert (1, 2) == butlast({1, 2, 3})
    assert ((1, "a"), (2, "b")) == butlast({1: "a", 2: "b", 3: "c"})
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

