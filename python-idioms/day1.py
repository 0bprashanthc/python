#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Enumerate():
    a = [1,2,3,4]
    #BAD: you could use for loop
    for i in range(0,len(a)):
        print i, a[i]
     
    #BAD: you could use while loop
    i = 0
    while i < len(a):
        print i,a[i]
        i += 1

    #GOOD: use emumerate
    for index, item in enumerate(a):
        print index, item

def iterableFile(file):
    #file handles are iterable !
    for line in open(file):
        print line.rstrip()

def basicDataTypes():
    #'tuples' are all over the place
    #For example, this code for swapping two numbers implicitly uses tuples
    a,b = 4,3
    a,b = b,a
    print a==3, b==4

    #'lists' keep track of stuff
    x = []
    x.append(5) #[5]
    x.extend([3,4,6]) #[5,3,4,6]
    x.reverse() #[6,4,3,5]

    #sort() for list of tuples
    '''
        The sort method will run cmp on each of the tuples, 
            which sort on the first element of each tuple
    '''
    y = [('n',23),('d',1),('a',87)]
    #y.sort() or y.sort(cmp) both are same
    y = y.sort() #[('a',87),('d',1),('n',23)]
    '''
        To sort the list on different element than default 
        first element, cmp function can be passed explicitily
    '''
    def sort_on_second(a,b):
        return cmp(a[1],b[1])

    y = y.sort(sort_on_second) #[('d',1),('n',23),('a',87)]


   #'dictionaries' get() for maintaining keys with multiple values
   '''
        given the below data in a file:
        a 1
        b 3
        c 4
        a 2
        d 6
        you could use below to store it in dictionary,
            but the value gets return for same key

        for line in open(file):
            key, value = line.split()
            d[key] = value

        lets say, you want a list of values for a given key
    '''
    d = {}
    for line in open(file):
        key, value = line.split()
        l = d.get(key, [])
        l.append(int(value))
        d[key] = l

    '''
        if dict has keys with list of values and you need to 
            sort the dict items based on the sum of values list
    '''
    def sort_on_sum(a,b):
        return cmp(sum(a[1]),sum(b[1]))

    items = d.items()
    items = items.sort(sort_on_sum)

