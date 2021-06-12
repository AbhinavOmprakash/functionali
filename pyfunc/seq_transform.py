"""Functions that transform sequences"""
from typing import Callable, Iterable, Generator, Any, Tuple
from functools import reduce

def conj(iterable:Iterable, *args:Any)-> Iterable:
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

def fmap(function: Callable, arguments: Iterable, *args: Iterable) -> Generator:
    """Similar to Python's map, but combines star_map."""
    pass


def argmap(functions: Iterable[Callable], *args:Any) -> Generator:
    """Maps an argument(s) to multiple functions."""
    pass


def argzip(sequence: Iterable[Callable], *args:Any) -> Generator:
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

    #TODO find better name for split?
    def split(constructed, inner_lis): 
        #constructed is a nested list like [[1,2,3], ['a','b','c']]
        return tuple(map(conj, constructed, inner_lis))

    def create_nested_list(sequence):
        # to be passed as an initial value to reduce
        # the number of 2nd level lists corresponds
        # to the number of elements in the inner list
        # of sequence. for e.g
        # [ [1,'a'], [2,'b], [3,'c'] ] -> ( (), () )
        
        return (() for i in range(len(sequence[0])))

    return reduce(split, sequence, create_nested_list(sequence))

def interleave(seq1: Iterable, seq2: Iterable, *seqs: Iterable) -> Generator:
    """Similar to clojure's interleave."""
    pass


def flatten(sequence: Iterable) -> Generator:
    """Similar to clojure's flatten. Returns the contents of a nested sequence as a flat sequence.
    Flatten is recursive."""
    pass
