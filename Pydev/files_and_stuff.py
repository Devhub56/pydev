#!/usr/bin/env python
import fileinput

f = open("some_file.txt", "a")
f.write("Now the file has  some more content!")
f.close()

#open and read the file after the appending:
f = open("some_file.txt", "r")
print(f.read())

f = open("/home/fel/Pydev/files_and_stuff.py", "r")
print(f.read())
f.close()

#better written as
f=open("some_dimwit_file.txt","a")
try:
    f.write("Now the file has  some  content!")
finally:
    f.close()
#variant 2
with open("some_file.txt") as somefile:
#     do_something(somefile)
#iterating over file contents
 def process(string):
        print('Processing:', string)

with open("some_file.txt") as f:
    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)
#Alternate way of writing the loop above though we want to avoid the break as much as often to make the code more readable
with open("some_file.txt") as f:
    while True:
        char = f.read(1) #read the whole th
        if not char: break
        process(char)
#reading a line in a file using the readline methodswith open(filename) as f:
while True:
    line = f.readline()
    if not line: break
    process(line)
#the lazy way
for line in fileinput.input("some_file.txt"):
    process(line)
