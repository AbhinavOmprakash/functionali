from functionali import (
    cons, 
    conj,
    concat,
    argzip,
    unzip,
    interleave,
    flatten,
)

from collections import deque


def test_cons():
    assert deque([3,1,2]) == cons(3, [1,2])
    assert deque([(3, "c"), (1, "a"), (2, "b")]) == cons((3, "c"), {1:"a", 2: "b"})
    assert deque([3,1,2]) == cons(3, {1,2})
    assert deque([3,1,2]) == cons(3, deque([1,2]))
    

def test_conj():
    assert [1, 2, 3, 4, 5] == conj([1,2,3,4],5)
    assert [1, 2, 3, 4, 5, 6, 7, 8] == conj([1,2,3,4],5,6,7,8)
    assert [1, 2, 3, 4, [5, 6, 7]] == conj([1,2,3,4],[5,6,7])
    assert (1, 2, 3, 4, 5, 6, 7) == conj((1,2,3,4),5,6,7)
    assert (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11) == conj(range(10), 11)
    assert {1: 'a', 2: 'b', 3: 'c'} == conj({1:"a", 2:"b"}, {3:"c"})
    assert deque([3,1,2]) == conj(deque([1,2]), 3)
    assert deque([4, 3,1,2]) == conj(deque([1,2]), 3,4)


def test_concat():
    # The difference between concat And conj is seen 
    # only with a deque, it makes sense only test a deque.
    assert deque([1,2,3]) == concat(deque([1,2]),3)
    assert deque([1,2,3,4]) == concat(deque([1,2]), 3,4)
    assert deque([4,3,1,2]) != concat(deque([1,2]), 3,4)