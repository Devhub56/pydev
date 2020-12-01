#! usr/bin/env python

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

age=int(input('Enter your age : '))
assert 0 < age < 120, 'The age must be realistic , Adios BUFF'
if age<5:
    print('You are too young Kiddo !')
elif 6<=age<=120:
    print('Welcome Oldie')
#iterating over dictionaries
d = {'x': 1, 'y': 2, 'z': 3}
for key, value in d.items():
    print(key, 'corresponds to', value)
#parallel iteration
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
#zip testing
list(zip(names, ages))

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
#Now we can unpack the tuples in our loop.
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
#iteratingoverstrings using the enumerate method
index = 0
for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'
