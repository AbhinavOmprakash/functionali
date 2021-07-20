
Welcome to Functionali's documentation!
=======================================

.. image:: https://codecov.io/gh/AbhinavOmprakash/functionali/branch/main/graph/badge.svg?token=75LLE4F7EY
   :target: https://codecov.io/gh/AbhinavOmprakash/functionali
    
.. image:: https://readthedocs.org/projects/functionali/badge/?version=latest
   :target: https://functionali.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
      
Functional programming is a fundamentally different way of solving problems, and once It clicks, it's pure joy after that. This library is my effort to bring that joy to the python community.
A lot of ideas in this library have been taken from Clojure and Haskell, so the credit goes to those languages. 
If you find your favorite function missing, or find ways to improve this project, I'd love to hear it.

There are quite a few functions in the library, And they can seem quite overwhelming at first.
These functions can be divided into four major categories-

#. Higher order functions. For example ``foldr``, ``curry``, ``flip``, 
#. Sequence traversing functions. For example ``first``, ``rest``, ``last``.
#. Sequence transforming functions. For example ``cons``, ``concat``, ``flatten``.
#. predicates. For example ``is_even``, ``is_prime``, ``is_nested``.


Besides this, the library provides a few "experimental" functions.
But don't worry about these if you are just getting started.


.. toctree::
   :maxdepth: 2

   seq-traverse
   seq-transform
   predicates
   higher-order-functions
   experimental



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
