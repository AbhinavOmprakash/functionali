"""Functions that transform sequences"""
from functools import reduce
from .predicates import is_atom, is_nested, not_
from collections import deque

from typing import (
    Callable,
    Iterable,
    Generator,
    Any,
    Tuple,
    Union,
    Dict,
    Tuple,
    List,
)


def cons(arg: Any, iterable: Iterable) -> deque:
    """Returns a deque with arg as the first element.

    Adds to the left of a deque.

    >>> cons(5, [1,2,3,4])
    deque([5, 1, 2, 3, 4])

    >>> cons(3, deque([1,2]))
    deque([3, 1, 2])

    >>> cons((3, "c"), {1:"a", 2: "b"})
    deque([(3, "c"), (1, "a"), (2, "b")])

    """

    if isinstance(iterable, dict):
        dq = deque(iterable.items())
    else:
        dq = deque(iterable)

    dq.appendleft(arg)

    return dq


def conj(iterable: Iterable, *args: Any) -> Iterable:
    """Short for conjoin, adds element to the iterable, at the appropriate end.
    Adds to the left of a deque.

    >>> conj([1,2,3,4],5)
    [1, 2, 3, 4, 5]

    >>> conj(deque([1,2]), 3,4)
    deque([4, 3, 1, 2])

    >>> conj([1,2,3,4],5,6,7,8)
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> conj([1,2,3,4],[5,6,7])
    [1, 2, 3, 4, [5, 6, 7]]

    >>> conj((1,2,3,4),5,6,7)
    (1, 2, 3, 4, 5, 6, 7)

    >>> conj(range(10), 11)
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11)

    >>> conj({1:"a", 2:"b"}, {3:"c"})
    {1: 'a', 2: 'b', 3: 'c'}

    """
    if isinstance(iterable, list):

        return iterable + list(args)  # since args is a tuple

    elif isinstance(iterable, tuple):
        return iterable + args

    elif isinstance(iterable, dict):
        # Make a copy of iterable, instead of mutating it.
        conjed_dict = {**iterable}

        for d in args:
            conjed_dict.update(d)

        return conjed_dict

    elif isinstance(iterable, set):
        return {*iterable, *args}

    elif isinstance(iterable, deque):
        dq = deque(iterable)
        for element in args:
            dq.appendleft(element)
        return dq

    else:
        return tuple(iterable) + args


def concat(iterable, *args):
    """Add items to the end of the iterable.

    >>> concat([1,2,3,4],5)
    [1, 2, 3, 4, 5]
    >>> concat(deque([1,2]), 3,4)
    deque([1, 2, 3, 4])

    """

    if isinstance(iterable, deque):
        dq = deque(iterable)

        for element in args:
            dq.append(element)

        return dq

    else:
        # Since conj Behavior for data Structures other than
        # deque are similar to concat behaviour.
        # call conj
        return conj(iterable, *args)


def argzip(sequence: Iterable[Callable], *args: Any) -> Generator:
    """
    Similar to zip, but instead of zipping iterables,
    It zips an argument(s) with all the values of the iterable.
    for example.
    >>> list(argzip([1,2,3,4], "number"))
    [(1, 'number'), (2, 'number'), (3, 'number'), (4, 'number')]

    >>> list(argzip([1,2,3,4], "number", "int"))
    [(1, 'number', 'int'), (2, 'number', 'int'), (3, 'number', 'int'), (4, 'number', 'int')]
    """
    return ((a, *args) for a in sequence)


def unzip(sequence: Iterable) -> Tuple[Any]:
    """Opposite of zip. Unzip is shallow.
    >>> unzip([[1,'a'], [2,'b'], [3,'c']])
    ((1, 2, 3), ('a', 'b', 'c'))
    >>> unzip([ [1,'a','A'], [2, 'b','B'], [3,'c','C'] ])
    ((1, 2, 3), ('a', 'b', 'c'), ('A', 'B', 'C'))

    shallow nature of unzip.
    >>> unzip([ [[1,'num'],['a','str']], [[2,'num'],['b','str']] ])
    (([1, 'num'], [2, 'num']), (['a', 'str'], ['b', 'str']))
    """

    # TODO find better name for split?
    def split(constructed, inner_lis):
        # constructed is a nested list like [[1,2,3], ['a','b','c']]
        return tuple(map(conj, constructed, inner_lis))

    def create_nested_list(sequence):
        # to be passed as an initial value to reduce
        # the number of 2nd level lists corresponds
        # to the number of elements in the inner list
        # of sequence. for e.g
        # [ [1,'a'], [2,'b], [3,'c'] ] -> ( (), () )

        return (() for i in range(len(sequence[0])))

    return reduce(split, sequence, create_nested_list(sequence))


def interleave(*seqs: Iterable) -> Tuple:
    """Similar to clojure's interleave. returns a flat sequence with the contents of iterables interleaved.
    >>> interleave([1,2,3],["a","b","c"])
    (1, 'a', 2, 'b', 3, 'c')

    >>> interleave([1,2,3],["int","int","int"], ["a","b","c"],["str","str","str" ])
    (1, 'int', 'a', 'str', 2, 'int', 'b', 'str', 3, 'int', 'c', 'str')
    """
    return flatten(zip(*seqs))


def flatten(sequence: Iterable) -> Tuple:
    """Returns the contents of a nested sequence as a flat sequence.
    Flatten is recursive.
    >>> flatten([1,2,[3,[4],5],6,7])
    (1, 2, 3, 4, 5, 6, 7)"""

    # TODO find better name
    def inner_fn(initial_val, elem):
        if is_atom(elem):
            return conj(initial_val, elem)
        elif is_nested(elem):
            # recursively call flatten if elem is a nested list
            return conj(initial_val, *flatten(elem))
        else:
            return conj(initial_val, *elem)

    return reduce(inner_fn, sequence, ())


def take_while(predicate: Callable, iterable: Iterable) -> Tuple:
    """
    >>> take_while(is_even, [2,4,6,7,8,9,10])
    (2,4,6)

    >>> def is_even_dict(d):
            #checks if the key of dict d is even
            return d[0]%2==0
    >>> take_while(is_even_dict, {2:"a", 4:"b",5:"c"})
        ((2, "a"), (4, "b"))
    """

    if isinstance(iterable, dict):
        it = iter(iterable.items())
    else:
        it = iter(iterable)

    accumulator = []
    elem = next(it)
    while predicate(elem):
        accumulator.append(elem)
        elem = next(it)

    return tuple(accumulator)


def drop_while(predicate: Callable, iterable: Iterable) -> Tuple:
    """
    >>> drop_while(is_even, [2,4,6,7,8,9,10])
    (7,8,9, 10)

    >>> def is_even_dict(d):
            #checks if the key of dict d is even
            return d[0]%2==0
    >>> drop_while(is_even_dict, {2:"a", 4:"b",5:"c"})
        ((5, "c"),)
    """

    if isinstance(iterable, dict):
        it = iter(iterable.items())
    else:
        it = iter(iterable)

    elem = next(it)
    while predicate(elem):
        # discard values
        elem = next(it)

    # Since elem is the first element
    # that fails the predicate.
    # and the iterator has already moved ahead.
    # we need to include elem
    return (elem,) + tuple(it)


def split_with(predicate: Callable, iterable: Iterable) -> Tuple[Tuple]:
    # consider implementing with reduce
    # since we are iterating through iterable twice.
    return (take_while(predicate, iterable), drop_while(predicate, iterable))


def insert(
    element: Any, iterable: Iterable, *, key: Callable = lambda x: x
) -> Iterable:
    """Inserts `element` right before the first element
    in the iterable that is greater than `element`

    >>> insert(3, [1,2,4,2])
    (1,2,3,4,2)

    >>> insert((2, "b"), {1:"a", 3:"c"})
    ((1, "a"), (2, "b"), (3, "c"))

    Using the key Parameter
    >>> Person = namedtuple("Person", ("name", "age"))

    >>> person1 = Person("John", 18)
    >>> person2 = Person("Abe", 50)
    >>> person3 = Person("Cassy", 25)

    >>> insert(person3, (person1, person2), key=lambda p:p.age)
        (person1, person3, person2)

    >>> insert(person3, (person1, person2), key=lambda p:p.name)
        (person3, person1, person2)

    """
    if isinstance(iterable, dict):
        it = iter(iterable.items())
    else:
        it = iter(iterable)

    accumulator = []
    elem = next(it)

    while key(elem) <= key(element):
        accumulator.append(elem)
        elem = next(it)

    return tuple(accumulator) + (element, elem) + tuple(it)
