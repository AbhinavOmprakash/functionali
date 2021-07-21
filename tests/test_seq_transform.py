from functionali import (
    cons,
    conj,
    concat,
    argzip,
    argmap,
    unzip,
    interleave,
    flatten,
    insert,
    remove,
)

from collections import deque, namedtuple


def test_cons():
    assert cons(3, []) == deque([3])
    assert deque([3, 1, 2]) == cons(3, [1, 2])
    assert deque([(3, "c"), (1, "a"), (2, "b")]) == cons((3, "c"), {1: "a", 2: "b"})
    assert deque([3, 1, 2]) == cons(3, {1, 2})
    assert deque([3, 1, 2]) == cons(3, deque([1, 2]))


def test_conj():
    assert conj([], 1) == [1]
    assert [1, 2, 3, 4, 5] == conj([1, 2, 3, 4], 5)
    assert [1, 2, 3, 4, [5]] == conj([1, 2, 3, 4], [5])
    assert [1, 2, 3, 4, 5, 6, 7, 8] == conj([1, 2, 3, 4], 5, 6, 7, 8)
    assert [1, 2, 3, 4, [5, 6, 7]] == conj([1, 2, 3, 4], [5, 6, 7])
    assert (1, 2, 3, 4, 5, 6, 7) == conj((1, 2, 3, 4), 5, 6, 7)
    assert (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11) == conj(range(10), 11)
    assert {1: "a", 2: "b", 3: "c"} == conj({1: "a", 2: "b"}, {3: "c"})
    assert {1, 2, 3} == conj({1, 2}, 3)
    assert deque([3, 1, 2]) == conj(deque([1, 2]), 3)
    assert deque([4, 3, 1, 2]) == conj(deque([1, 2]), 3, 4)


def test_concat():
    assert concat((), 1) == (1,)
    assert [1, 2, 3, 4, 5] == concat([1, 2, 3, 4], 5)

    # The difference between concat And conj is seen
    # only with a deque, it makes sense only test a deque.
    assert deque([1, 2, 3]) == concat(deque([1, 2]), 3)
    assert deque([1, 2, 3, 4]) == concat(deque([1, 2]), 3, 4)
    assert deque([4, 3, 1, 2]) != concat(deque([1, 2]), 3, 4)


def test_argmap():
    inc = lambda x: x + 1
    dec = lambda x: x - 1

    assert list(argmap([inc, dec], [1])) == [2, 0]

    add = lambda a, b: a + b
    sub = lambda a, b: a - b

    assert list(argmap([add, sub], [2, 1])) == [3, 1]


def test_argzip():
    assert [(1, "number"), (2, "number"), (3, "number"), (4, "number")] == list(
        argzip([1, 2, 3, 4], "number")
    )
    assert [
        (1, "number", "int"),
        (2, "number", "int"),
        (3, "number", "int"),
        (4, "number", "int"),
    ] == list(argzip([1, 2, 3, 4], "number", "int"))


def test_unzip():
    assert ((1, 2, 3), ("a", "b", "c")) == unzip([[1, "a"], [2, "b"], [3, "c"]])
    assert ((1, 2, 3), ("a", "b", "c"), ("A", "B", "C")) == unzip(
        [[1, "a", "A"], [2, "b", "B"], [3, "c", "C"]]
    )
    assert (([1, "num"], [2, "num"]), (["a", "str"], ["b", "str"])) == unzip(
        [[[1, "num"], ["a", "str"]], [[2, "num"], ["b", "str"]]]
    )


def test_interleave():
    assert (1, "a", 2, "b", 3, "c") == interleave([1, 2, 3], ["a", "b", "c"])
    assert (
        1,
        "int",
        "a",
        "str",
        2,
        "int",
        "b",
        "str",
        3,
        "int",
        "c",
        "str",
    ) == interleave(
        [1, 2, 3], ["int", "int", "int"], ["a", "b", "c"], ["str", "str", "str"]
    )


def test_flatten():
    assert (1, 2, 3, 4, 5, 6, 7) == flatten([1, 2, [3, [4], 5], 6, 7])


def test_insert():
    assert insert(2, []) == (2,)
    assert (1, 2, 3, 4) == insert(3, [1, 2, 4])
    assert (1, 2, 3, 4, 2) == insert(3, [1, 2, 4, 2])
    assert (1, 2, 3, 4) == insert(4, [1, 2, 3])
    assert ((1, "a"), (2, "b"), (3, "c")) == insert((2, "b"), {1: "a", 3: "c"})

    # for the key parameter
    Person = namedtuple("Person", ("name", "age"))
    person1 = Person("John", 18)
    person2 = Person("Abe", 50)
    person3 = Person("Cassy", 25)
    assert (person1, person3, person2) == insert(
        person3, (person1, person2), key=lambda p: p.age
    )
    assert (person3, person1, person2) == insert(
        person3, (person1, person2), key=lambda p: p.name
    )


def test_remove():
    is_pos = lambda x: x >=0
    assert list(remove(is_pos, range(-5,5))) == [-5,-4,-3,-2,-1]