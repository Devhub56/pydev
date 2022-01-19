#!/usr/bin/python3
#checks or several instances of lowercase in a supplied string.
def any_lowercase1(somestring):
    # Checks only first letter in string if it is lowercase or not and returns
    # boolean.
    for c in somestring:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(someotherstring):
    # Checks if string 'c' is lowercase or not; and returns string 'True';
    # Returns 'True' everytime, given argument does not matter;
    for c in someotherstring:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(somestring):
    # Checks if each letter in string is lowercased or not and assigned the outcome
    # (boolean value) to the variable 'flag'; new value is assigned to 'flag' with
    # every checked letter;
    # Returns boolean value of calling islower() method on only the last letter
    # of the given string;
    for c in somestring:
        flag = c.islower()
    return flag

def any_lowercase4(somestring):
    # Checks if there is ANY lowercased letter in given string and returns boolean;
    flag = False
    for c in somestring:
        flag = flag or c.islower()
    return flag

def any_lowercase5(somestring):
    # Checks every letter if it is not lowercased and returns boolean if all the
    # letters in string are lowercased or not;
    for c in somestring:
        if not c.islower():
            return False
    return True
