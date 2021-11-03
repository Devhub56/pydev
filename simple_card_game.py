#!/usr/bin/env python
from pprint import pprint
from random import shuffle

#some random dice throwing

from random import randrange
num   = int(input('How many dice? '))
sides = int(input('How many sides per die? '))
sum = 0
for i in range(num): sum += gamble(sides) + 1
print(f'The result is {sum}')

#shuffling cards
values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]
shuffle(deck)
pprint(deck[:12])
#dealing a card whenever the Enter key is pressed
while deck:
    input(deck.pop())
