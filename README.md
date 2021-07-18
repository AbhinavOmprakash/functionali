# Functionali
functional programming tools for python. We try to put the fun in functional programming 😉

[![codecov](https://codecov.io/gh/AbhinavOmprakash/functionali/branch/main/graph/badge.svg?token=75LLE4F7EY)](https://codecov.io/gh/AbhinavOmprakash/functionali)

[![Documentation Status](https://readthedocs.org/projects/functionali/badge/?version=latest)](https://functionali.readthedocs.io/en/latest/?badge=latest)
      

Functional programming is a fundamentally different way of solving problems, and once It clicks, it's pure joy after that. This library is my effort to bring that joy to the python community.
A lot of ideas in this library have been taken from Clojure and Haskell, so the credit goes to those languages. 
If you find your favorite function missing, or find ways to improve this project, I'd love to hear it.

## a few examples to whet your appetite

Functionali provides functions to traverse sequences(Including dictionaries), Some of the most useful ones are `first`, `rest`, `last`,`butlast`, `take`, `drop`
```Python
from functionali import first, rest, last, butlast, take, drop

>>> first([1,2,3,4,5])
    1

>>> first({1:"a", 2:"b"})
    (1, "a")

>>> last([1,2,3,4])
    4

>>> list(rest([1,2,3,4,5]))
    [2, 3, 4, 5]

>>> butlast([1,2,3]) # returns all elements except the last element
    (1,2)

>>> take(3, [1,2,3,4,5])
    (1, 2, 3)

>>> drop(3, [1,2,3,4,5])
    (4,5)
```

There are functions that construct new sequences like `cons`, `conj`, `concat`, `insert`

```Python
from functionali import cons, conj, concat, insert
>>> cons(5, [1,2,3,4])
    deque([5, 1, 2, 3, 4]) # 5 is the 'head' of the new list.

# adds element to the iterable, at the appropriate end.
>>> conj([1,2,3,4],5) # similar to Clojure's conj
    [1, 2, 3, 4, 5]

    # Adds to the left of a deque.
>>> conj(deque([1,2]), 3,4)
    deque([4, 3, 1, 2])

# Add items to the end of the iterable.
>>> concat([1,2,3,4],5)
    [1, 2, 3, 4, 5]

>>> concat(deque([1,2]), 3,4)
    deque([1, 2, 3, 4])

# Inserts 3 right before the first element
# in the iterable (here:4) that is greater than 3
>>> insert(3, [1,2,4,2])
    (1,2,3,4,2)
```

Functionali also comes with a number of useful predicates 
(if You can't find something you're looking for, make a pull request.)
These can be combined in various ways.
for example.

```Python
from functionali import is_even, is_prime, take_while
>>> list(filter(is_even,[1,2,3,4])
    [2,4]

>>> take_while(is_prime, [2,3,5,4,6,5])) # Constructs a list while is_prime is true.
    [2,3,5]

```




