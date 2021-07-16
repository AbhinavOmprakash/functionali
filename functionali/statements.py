"""Expressions to substitute for Python statements"""
from typing import Any

# TODO Consider deleting this function
# def if_(bool_expr: bool, then_expr: Any, else_expr: Any = None):
#     """Created primarily to be used in lambda functions.

#     for e.g.
#     >>> f = lambda a,b : if_(a==b, "equality", "discrimination!")
#     >>> f(1,3)
#     'discrimination!'
#     >>> f(2,2)
#     'equality'

#     """

#     if bool_expr:
#         return then_expr
#     else:
#         return else_expr


def or_(arg, *args):
    """Lisp style ``or``. Evaluates expressions from left to right
    and returns the value of the first truthy expression.
    If all expressions evaluate to False, returns the value of the last expression.

    usage

    >>> or_(True, True, False)
    True
    >>> or_(True, False, False)
    True
    >>> or_(False, False, 0)
    0
    >>> or_(False, 0, False)
    False
    >>> or_(0,1,2,3,4,5)
    1
    >>> or_( "a"=="a", 5%2 )
    True
    >>> or_( "a"=="a", 5%5 )
    True
    >>> or_(1, [1,2,3,4,5,6,7])
    1
    >>> or_([], [1,2,3,4,5,6,7])
    [1, 2, 3, 4, 5, 6, 7]

    """
    if arg or not args:
        return arg

    else:
        for a in args:
            if a:
                return a
        # If none of the Arguments evaluates to true return the last one.
        return args[-1]


def and_(arg, *args):
    """Lisp style ``and``. Evaluates expressions from left to right
    and returns the value of the last truthy expression.
    If an expression evaluates to False, returns the value of the Falsey expression.

    usage

    >>> and_(True, True, False)
    False
    >>> and_(True, True, 2)
    2
    >>> and_(True, False, 2)
    False
    >>> and_(0,1,2,3,4,5)
    0
    >>> and_("a"=="a", 5%2)
    1
    >>> and_("a"=="a", 5%5)
    0
    >>> and_(1, [1,2,3,4,5,6,7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> and_([], [1,2,3,4,5,6,7])
    []
    """

    if not arg or not args:
        return arg

    else:
        for a in args:
            if not a:
                return a
        # return The last argument if all arguments were true.
        return args[-1]
