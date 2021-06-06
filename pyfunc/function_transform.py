"""higher order functions that consume other functions and return a modified function."""

from typing import Callable


def curry(fn: Callable) -> Callable:
    """Returns a curried version of the function."""
    pass


def partial(fn: Callable, *args, **kwargs) -> Callable:
    """Takes a function and fewer than normal arguments, and returns a function
    That will consume the remaining arguments and call the function"""

    def partial_fn(*rem_args, **rem_kwargs):
        return fn(*args, *rem_args, **kwargs ** rem_kwargs)

    return partial_fn
