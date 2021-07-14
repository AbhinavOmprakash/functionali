from functionali import (
    cons, 
    conj,
    concat,
    argzip,
    unzip,
    interleave,
    flatten,
    take_while,
    drop_while,
    split_with,
    insert,
)

from collections import deque, namedtuple


def test_cons():
    assert deque([3,1,2]) == cons(3, [1,2])
    assert deque([(3, "c"), (1, "a"), (2, "b")]) == cons((3, "c"), {1:"a", 2: "b"})
    assert deque([3,1,2]) == cons(3, {1,2})
    assert deque([3,1,2]) == cons(3, deque([1,2]))
    

def test_conj():
    assert [1, 2, 3, 4, 5] == conj([1,2,3,4],5)
    assert [1, 2, 3, 4, [5]] == conj([1,2,3,4],[5])
    assert [1, 2, 3, 4, 5, 6, 7, 8] == conj([1,2,3,4],5,6,7,8)
    assert [1, 2, 3, 4, [5, 6, 7]] == conj([1,2,3,4],[5,6,7])
    assert (1, 2, 3, 4, 5, 6, 7) == conj((1,2,3,4),5,6,7)
    assert (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11) == conj(range(10), 11)
    assert {1: 'a', 2: 'b', 3: 'c'} == conj({1:"a", 2:"b"}, {3:"c"})
    assert deque([3,1,2]) == conj(deque([1,2]), 3)
    assert deque([4, 3,1,2]) == conj(deque([1,2]), 3,4)


def test_concat():
    assert [1, 2, 3, 4, 5] == concat([1,2,3,4],5)
    # The difference between concat And conj is seen 
    # only with a deque, it makes sense only test a deque.
    assert deque([1,2,3]) == concat(deque([1,2]),3)
    assert deque([1,2,3,4]) == concat(deque([1,2]), 3,4)
    assert deque([4,3,1,2]) != concat(deque([1,2]), 3,4)


def test_argzip():
    assert [(1, 'number'), (2, 'number'), (3, 'number'), (4, 'number')] == list(argzip([1,2,3,4], "number"))
    assert [(1, 'number', 'int'), (2, 'number', 'int'), (3, 'number', 'int'), (4, 'number', 'int')] == list(argzip([1,2,3,4], "number", "int"))



def test_unzip():
    assert ((1, 2, 3), ('a', 'b', 'c')) == unzip([[1,'a'], [2,'b'], [3,'c']])
    assert ((1, 2, 3), ('a', 'b', 'c'), ('A', 'B', 'C')) == unzip([[1,'a','A'], [2, 'b','B'], [3,'c','C'] ])
    assert (([1, 'num'], [2, 'num']), (['a', 'str'], ['b', 'str'])) == unzip([[[1,'num'],['a','str']], [[2,'num'],['b','str']] ])


def test_interleave():
    assert (1, 'a', 2, 'b', 3, 'c') == interleave([1,2,3],["a","b","c"])
    assert (1, 'int', 'a', 'str', 2, 'int', 'b', 'str', 3, 'int', 'c', 'str') == interleave([1,2,3],["int","int","int"], ["a","b","c"],["str","str","str" ])


def test_flatten():
    assert (1, 2, 3, 4,5, 6, 7) == flatten([1,2,[3,[4],5],6,7])


def test_take_while():
    def is_even(n):
        return n%2==0

    def is_even_dict(d):
        #checks if the key of dict d is even
        return d[0]%2==0

    assert (2,4,6) == take_while(is_even, [2,4,6,7,8,9,10])
    assert () == take_while(is_even, [1,2,4,6,7,8,9,10])
    assert ((2, "a"), (4, "b")) == take_while(is_even_dict, {2:"a", 4:"b",5:"c"})


def test_drop_while():
    def is_even(n):
        return n%2==0

    def is_even_dict(d):
        #checks if the key of dict d is even
        return d[0]%2==0

    assert (7,8,9, 10) == drop_while(is_even, [2,4,6,7,8,9,10])
    assert (1,2,4,6,7,8,9,10) == drop_while(is_even, [1,2,4,6,7,8,9,10])
    assert ((5, "c"),) == drop_while(is_even_dict, {2:"a", 4:"b",5:"c"})


def test_split_with():
    def is_even(n): 
        return n%2==0

    assert ((2,4,6), (7,8,9, 10)) == split_with(is_even,[2,4,6,7,8,9,10])
    assert ((),(1,2,4,6,7,8,9,10)) == split_with(is_even,[1,2,4,6,7,8,9,10])


def test_insert():
    assert (1,2,3,4) == insert(3, [1,2,4])
    assert (1,2,3,4,2) == insert(3, [1,2,4,2])
    assert ((1, "a"), (2, "b"), (3, "c")) == insert((2, "b"), {1:"a", 3:"c"})

    # for the key parameter
    Person = namedtuple("Person", ("name", "age"))
    person1 = Person("John", 18)
    person2 = Person("Abe", 50)
    person3 = Person("Cassy", 25)
    assert (person1, person3, person2) == insert(person3, (person1, person2), key=lambda p:p.age)
    assert (person3, person1, person2) == insert(person3, (person1, person2), key=lambda p:p.name)
