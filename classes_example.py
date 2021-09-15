#!/usr/bin/env python
class person:
    def set_user_name(self,name):
        self.name=name

    def get_user_name(self):
        return self.name

    def greet_user(self):
        print ("Welcome,{}".format(self.name))

    def follow_up_user(self):
        print ("I hope you're progressing in your classes,{}".format(self.name))

Bella=person()
M=person()

User.set_user_name("User Name")
M.set_user_name("User ")

Bella.greet_user()
M.follow_up_user()
#Person.greet(User) is an alt when you know that User is a Person
#inheritance examples | super and sub class
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
    def init(self): # Overrides init method from Filter superclass
        self.blocked = ['SPAM']
#
#some multiple super classes
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print('Hi, my value is', self.value)
class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1 + -2 * 3//5')
tc.talk()
#exceptons
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
        except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break
#finally for housekeeping and cleanup
x = None
try:
    x = 1 / 0
finally:
    print('Cleaning up ...')
    del x
#CLASS OF HUMANS
