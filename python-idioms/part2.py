#!/usr/bin/env python
# -*- coding: utf-8 -*-

def listComprehension():
    #list of squares of even numbers between 0-8
    return [i*i for i in range(0,9) if i%2==0]

"""
    make any python class into a list iterable
        with two basic function:
            1. __getitem__
            2. __len__
"""
class MyList:
    def __init__(self, i):
        self.mylist = [None]*i

    def __getitem__(self, index):
        return self.mylist[index]

    def __len__(self):
        return len(self.mylist)

print "*****Executing iterable class*****"
obj = MyList(2)
print "Object : ", obj
print "Length : ", len(obj)
for index, item in enumerate(obj):
    print index, item

"""
    make any python class into a dict iterable
        with two basic functions:
            1. __getitem__
            2. __setitem__
"""
class MyDict:
    def __init__(self, key, value=None):
        self.d = {key:value}
        self.key = key

    def __getitem__(self, key):
        self.key = key
        return self.key

    def __setitem(self, key, value):
        self.d[key] = value
        return self.d

"""
    Iterators are a built-in type protocol for python
        any python class can be regarded as an iterator
        with two basic methods:
            1. __iter__
            2. next
"""
class basicIterator:
    def __init__(self, i, n):
        self.i = i
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.i

print "*****Executing iterator*****"
bi = basicIterator(0,3)
for i in bi:
    print i

"""
generators in python are implementations of coroutines
    Best used for iterators, looping for large iterable data
    It maintains the state of the iterable object
    to optimize the memory operations in the process
"""
def myGenerator(i):
    for i in range(0,i):
        yield i

print "*****Executing Generator*****"
for i in myGenerator(4):
    print i

"""
    assert is an useful python built-in keyword
    if something evaluates to True, it does nothing!
    if something evaluates to False, it raises AssertionError
        with support for custom messages
"""
def useAssert():
    a = [None]
    assert len(a) is not 1, "It should not be ONE"

useAssert()
