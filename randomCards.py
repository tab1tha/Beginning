#this program deals a pseudorandom card each time.
# real randomness can only be achieved using the urandom() function.
values=list(range(1,11)) +'Jack King Queen '.split()
suits='Hearts Spades Diamonds Clubs'.split()
deck=['{} of {}'.format(v,s) for v in values for s in suits]
from random import shuffle
shuffle(deck) #randomly rearranges the content of deck such that any possible outcome is equally probable.
print(deck)
while deck:input(deck.pop)
#to get Python to deal you a card each time you press Enter on your keyboard, until there are no
#more cards, you simply create a little while loop