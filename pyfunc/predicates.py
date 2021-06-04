"""A file containing useful predicates."""

from typing import List, Iterable, Callable, Any, Sequence
def is_even(num:int)->bool:
    return num%2==0

def is_odd(num:int)->bool:
    return num%2!=0

def is_prime(num:int)->bool:
    pass

def is_numeric(entity:Any)->bool:
    return any(map(isinstance, [entity, entity, entity], [int, float, complex]))

    
def contains(collection:Sequence, entity:Any)->bool:  
    """Checks whether collection contains the given entity."""
    return entity in collection

def is_empty(collection:Sequence)->bool:
    """Returns true if the collection is empty."""
    return not bool(collection)

def all_predicates(predicates:Iterable[Callable[[Any], bool]], entity:Any):
    """Checks if an entity satisfies all the predicates. Where entity is not a sequence."""
    return all((p(entity) for p in predicates))

def some_predicates(predicates:Iterable[Callable[[Any], bool]], entity:Any):
    """Checks if an entity satisfies any of the predicates. Where entity is not a sequence."""
    return any((p(entity) for p in predicates))

    