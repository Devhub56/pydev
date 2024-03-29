#!/usr/bin/env python3
def init(teammates):
    teammates['first']={}
    teammates['second']={}
    teammates['third']={}
    teammates['fourth'] = {}
storage = {}
init(storage)

def lookup(teammates,label,name):
    return teammates[label].get(name)

lookup(storage, 'second','someguy')

#another example
def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
MyNames  = {}
init(MyNames)
store(MyNames, 'Carlbot')
lookup(MyNames, 'middle', '')
