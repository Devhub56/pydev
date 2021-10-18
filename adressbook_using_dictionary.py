#!/usr/bin/env python3
from math import *
from future import *

name = input('Enter your name : ') or '<unknown>'
pwd = input('What is your password : ')
database= [['fel','6140'],
['james','2730']
]
if [name.lower(),pwd] in database: print(f"welcome ," {name} "," + "How can we help you today ?" )
else:
    print('Acess Denied !!')
    exit()
ask=input('What would you like to add to the db:')
db2=["some","unknown","user"]
db2[2:1]=(ask)
print (db2)
backup=db2.copy()
#dictionary methods
#simple dictionary
peeps={'fel':{'phone':'2730',
       'address':'Kampala Road'},
       'Jared':{'phone':'61441',
       'address':'Droid'},
       'Walid':{'phone':'8800',
       'address':'YouVersion'}
}
# Descriptive labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)? ')
# Use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# Only try to print information if the name is a valid key in
# our dictionary:
if name in peeps: print("{}'s {} is {}.".format(name, labels[key], peeps[name][key]))
# Use get to provide default values:
else:
    person = peeps.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, 'not available')
    print("{}'s {} is {}.".format(name, label, result))

#if and boolean operations
number = int(input('Enter a number between 1 and 10: '))
if number <= 10 and number >= 1:
    print('Great!')
else:
    print('Wrong!')
#Asssert methods
# assert condition, 'The age must be realistic'
#a loop to ensure that the user enters a name, as follows:
name = ''
while not name.strip():
     name = input('Please enter your name: ')
print('Hello, {}!'.format(name))
