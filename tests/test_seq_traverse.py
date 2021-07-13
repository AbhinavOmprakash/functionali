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
)


def test_first():
    assert 1 == first([1, 2, 3])
    assert 1 == first((1, 2, 3))
    assert 1 == first(set([1, 2, 3]))
    assert (1, "a") == first({1: "a", 2: "b"})
    assert None == first([])


def test_ffirst():
    assert 1 == ffirst([[1], [2], [3]])
    assert 1 == ffirst(((1,), (2,), (3,)))
    assert 1 == ffirst(set([(1, 2), (3, 4), (5, 6)]))
    assert None == ffirst([])


def test_last():
    assert 3 == last([1, 2, 3])
    assert 3 == last((1, 2, 3))
    assert 3 == last(set([1, 2, 3]))
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
    assert 2 == second(set([1, 2, 3]))
    assert (2, "b") == second({1: "a", 2: "b"})
    assert None == second([])
    # check that the last item is returned
    # when iterable is shorter than two
    assert 1 == second([1])


def test_third():
    assert 3 == third([1, 2, 3])
    assert 3 == third((1, 2, 3))
    assert 3 == third(set([1, 2, 3]))
    assert (3, "c") == third({1: "a", 2: "b", 3: "c"})
    assert None == third([])
    # check that the last item is returned
    # when iterable is shorter than Three
    assert 2 == third([1, 2])


def test_fourth():
    assert 4 == fourth([1, 2, 3, 4])
    assert 4 == fourth((1, 2, 3,4))
    assert 4 == fourth(set([1, 2, 3,4]))
    assert (4, "d") == fourth({1: "a", 2: "b", 3: "c", 4:"d"})
    assert None == fourth([])
    # check that the last item is returned
    # when iterable is shorter than Four
    assert 2 == fourth([1, 2])
    assert 3 == fourth([1, 2,3])


def test_fifth():
    assert 5 == fifth([1, 2, 3, 4, 5])
    assert 5 == fifth((1, 2, 3,4,5))
    assert 5 == fifth(set([1, 2, 3,4,5]))
    assert (5, "e") == fifth({1: "a", 2: "b", 3: "c", 4:"d", 5:"e"})
    assert None == fifth([])
    # check that the last item is returned
    # when iterable is shorter than five
    assert 2 == fifth([1, 2])
    assert 3 == fifth([1, 2,3])
    assert 4 == fifth([1, 2,3,4])

def test_butlast():
    assert (1, 2) == butlast([1, 2, 3])
    assert (1, 2) == butlast((1, 2, 3))
    assert (1, 2) == butlast(set([1, 2, 3]))
    assert ((1, "a"), (2, "b")) == butlast({1: "a", 2: "b", 3: "c"})
    assert None == butlast([])
