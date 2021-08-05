# Write a program that generates a list L of 50 randomn numbers between 1 and 100
from random import randint
L = [randint(1, 101) for i in range(50)]

# Count how many items in a list L that are greater than 50:
count = len([i for i in L if i > 50])
print(count)


# Given a list L that contains numbers between 1 and 100, create a new list whose first element is how many ones are in L, whose second element is how many twos are in L, etc
L = input('give a list of numbers between 1 and 100: ')
frequencies = [L.count(i) for i in range(1, 101)]


# Join method can often be used with list comprehensions to quickily build up a string. Create a string that contains a random assortment of 1000 letters
from random import choice
alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = ''.join([choice(alphabet) for i in range(1000)])

# Flip order: Suppose we have a list whose elements are lists of size 2.
L = [[1,2], [3,4], [5,6]]
M = [[y,x] for x,y in L]
        
