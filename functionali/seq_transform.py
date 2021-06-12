"""Functions that transform sequences"""
from typing import Callable, Iterable, Generator, Any, Tuple
from functools import reduce
from .predicates import is_atom, is_nested


def conj(iterable: Iterable, *args: Any) -> Iterable:
    """>>> conj([1,2,3,4],5)
    [1, 2, 3, 4, 5]
    >>> conj([1,2,3,4],5,6,7,8)

    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> conj([1,2,3,4],[5,6,7,])

    [1, 2, 3, 4, [5, 6, 7]]
    >>> conj((1,2,3,4),5,6,7)
    (1, 2, 3, 4, 5, 6, 7)
    >>> conj((i for i in range(10)),11)
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11)
    >>> conj({1:"a", 2:"b"}, {3:"c"})


    """
    if isinstance(iterable, list):
        return iterable + list(args)
    elif isinstance(iterable, tuple):
        return iterable + args
    # elif isinstance(iterable, dict):
    #     return {**iterable, **(*args)}
    else:
        return tuple(iterable) + args


def argmap(functions: Iterable[Callable], *args: Any) -> Generator:
    """Maps an argument(s) to multiple functions."""
    pass


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
    >>> (interleave([1,2,3],["a","b","c"])
    (1, 'a', 2, 'b', 3, 'c')
    >>> interleave([1,2,3],["int","int","int"], ["a","b","c"],["str","str","str" ])
    (1, 'int', 'a', 'str', 2, 'int', 'b', 'str', 3, 'int', 'c', 'str')
    """
    return flatten(zip(*seqs))


def flatten(sequence: Iterable) -> Tuple:
    """Similar to clojure's flatten. Returns the contents of a nested sequence as a flat sequence.
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


if __name__ == "__main__":
    a = tuple(zip([1, 2, 3], ["a", "b", "c"]))
    print(flatten(a))
