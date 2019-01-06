#/usr/bin/env python
# -*- coding: utf-8 -*-


def any_all():
    """
        'any' and 'all' are built-in python keywords
        They operate on iterables like lists, generators
        any - returns True if any element of the iterable is 
                True (and False otherwise);
        all - returns True if all elements of the iterable 
                are True (and False otherwise);
    """
    x = [ True, False ]
    print any(x),all(x)
    y = [ True, True ]
    print any(x),all(x)
    z = [ False, False ]
    print any(z),all(z)

