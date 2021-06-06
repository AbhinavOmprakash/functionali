"""Functions that transform sequences"""
from typing import Callable, Iterable, Generator


def fmap(function: Callable, arguments: Iterable, *args) -> Generator:
    """Similar to Python's map, but combines star_map."""
    pass


def argmap(functions: Iterable[Callable], arg: Any, *args) -> Generator:
    """Maps an argument(s) to multiple functions."""
    pass


def argzip(sequence: Iterable[Callable], arg: Any, *args) -> Generator:
    """Similar to zip, but instead of zipping iterables,
    It zips An argument with all the values of their iterable.
    for example argzip([1,2,3], "number") -> ( (1,"number"), (2,"number"),(3,"number") )"""
    pass


def unzip(sequence: Iterable) -> Generator:
    """Opposite of zip. Unzip is shallow."""
    pass


def interleave(seq1: Iterable, seq2: Iterable, *seqs: Iterable) -> Generator:
    """Similar to clojure's interleave."""
    pass


def flatten(sequence: Iterable) -> Generator:
    """ Similar to clojure's flatten. Returns the contents of a nested sequence as a flat sequence"""
    pass
