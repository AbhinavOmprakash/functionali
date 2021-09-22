from typing import Callable, Any, Iterable, Union
from inspect import signature
from functools import partial, reduce
from .seq_traverse import reversed_


def flip(fn: Callable) -> Callable:
    """returns a function that takes in a flipped order of args.
    Usage:

    >>> f = lambda a,b : a-b
    >>> f(1,3)
    -2
    >>> f(3,1)
    2
    >>> flipped_f = flip(f)
    >>> flipped_f(3,1)
    -2
    >>> flipped_f(1,3)
    2

    Added in version: 0.1.0
    """

    def flipped(*args, **kwargs):
        return fn(*reversed_(args), **kwargs)

    return flipped


def foldr(fn: Callable, iterable: Iterable, initial: Any = None) -> Any:
    """Fold right. Stack safe implementation

    Added in version: 0.1.0
    """
    # Implement with reduce, for this we reverse the iterable
    # and then we flip fn since the Function signature for fn is fn(element, accumulator)
    # This is the standard function signature of any function passed to Foldright
    # the flipping is necessary because reduce expects the reducing function to have a function signature of
    # fn(accumulator, element) Which is the opposite of fn(element, accumulator)
    reversed_it = reversed_(iterable)

    if initial is None:
        initial = next(reversed_it)

    return reduce(flip(fn), reversed_it, initial)


def comp(*fns: Callable):
    """
    returns a composed function that takes a variable number of args,
    and applies it to ``fns`` passed from right to left.

    Added in version: 0.1.2
    """

    def composed(*args, **kwargs):
        first_func = fns[-1]  # since we are applying functions from right to left
        return foldr(lambda f, arg: f(arg), fns[:-1], first_func(*args, **kwargs))

    return composed


def curry(fn: Callable) -> Callable:
    """Returns a curried version of the function.

    >>> def fn(arg1, arg2, arg3):  # test function
        return [arg1, arg2, arg3]
    >>> curried_fn = curry(fn)
    >>> curried_fn(1)(2)(3)
        [1, 2, 3]

    Added in version: 0.1.0
    """
    num_args = len(signature(fn).parameters)

    def curried(arg, fn, num_args):
        if num_args <= 1:
            # call fn if the final arg is passed
            return fn(arg)
        else:
            # call partial fn if not final arg
            f = partial(fn, arg)
            return lambda arg: curried(arg, f, num_args - 1)

    return lambda arg: curried(arg, fn, num_args)


def trampoline(fn: Callable, *args: Any):
    """takes a function ``fn`` and calls if with ``*args``. if ``fn`` returns a function,
    calls the function until a function is not returned i.e. the base case is reached.
    function ``fn`` must return a function in its recursive case.
    Useful for optimizing tail recursive functions or mutual recursions.


    >>> def fact(x, curr=1, acc=1):
    >>>    if curr == x:
    >>>        return curr*acc
    >>>    else:
    >>>        return lambda: fact(x, curr+1, acc*curr)

    >>> trampoline(fact, 3) == 6
    >>> trampoline(fact, 100000000000) # does not raise RecursionError
    """
    recursive_fn = fn(*args)
    while isinstance(recursive_fn, Callable):
        recursive_fn = recursive_fn()
    return recursive_fn


def threadf(arg:Any, forms:Iterable[Union[Callable, Iterable]]) -> Any :
    #TODO improve docstrings.
    """thread first, passes ``arg`` as the first argument to the first function in ``forms``
    and passes the result as the first argument to the second form and so on."""

    def fn(result, form):
        if isinstance(form, Iterable):
            fn = form[0]
            args = form[1:]
            return fn(result, *args)
        else:
            return form(result)

    return reduce(fn, forms, arg)

def threadl(arg:Any, forms:Iterable[Union[Callable, Iterable]]) -> Any:
    """Thread last, passes ``arg`` as the last argument to the first function in ``forms``
    and passes the result as the last argument to the second form and so on."""

    def fn(result, form):
        if isinstance(form, Iterable):
            fn = form[0]
            args = form[1:]
            return fn(*args, result,)
        else:
            return form(result)

    return reduce(fn, forms, arg)