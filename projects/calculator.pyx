#!/usr/bin/env python
from math import pi as pie
from random import randrange as gamble

class man:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print ("Man needs bread")
            self.hungry=False
        else:
            print ("Man doesn't live on bread alone...")
class talking_man(man):
    def __init__(self):
        super().__init__()
        self.sound = 'Aha..I can talk!'
    def sing(self):
        print(self.sound)
    #infinte sequence
    def check_index(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError
class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start   - the first value in the sequence
        step    - the difference between two adjacent values
        changed - a dictionary of values that have been modified by
                  the user
        """
        self.start = start                        # Store the start value
        self.step = step                          # Store the step value
        self.changed = {}                         # No items have been modified
    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        check_index(key)
        try:
            return self.changed[key]             # Modified?
        except KeyError:                          # otherwise ...
            return self.start + key * self.step   # ... calculate the value
    def __setitem__(self, key, value):
        """
        Change an item in the arithmetic sequence.
        """
        check_index(key)
        self.changed[key] = value                 # Store the changed value

s = ArithmeticSequence(1, 1)
print(s[5])
#subclassing Any methods not overridden by CounterList (such as append, extend, index, and so on) may be used directly. In the two methods that are overridden, super is used to call the superclass version of the method, adding only the necessary behavior of initializing the counter attribute (in __init__) and updating the counter attribute (in __getitem__).
#class CounterList(list):
#    def __init__(self, *args):
#        super().__init__(*args)
#        self.counter = 0
#    def __getitem__(self, index):
#        self.counter += 1
#        return super(CounterList, self).__getitem__(index)

class circle:
    def __init__(self):
        self.p=pie
        self.r=float(input('Enter Radius of Circle : '))
        assert 0 < self.r , 'The radius of the circle must be realistic , pleasec check your value and try again!'
    def set_size(self,size):
        self.p,self.r = size
    def get_size(self):
        return self.p, self.r
    size = property(get_size, set_size)
    
class circle_area(circle):
    def __init__(self):
        circle.__init__(self)
        self.area= self.p*((self.r)*(self.r))
    def result(self):
        print(self.area)

