# Creating lists:
l = []

# Use eval(input()) to allow the user to enter a list:
L = eval(input('Enter a list: '))
Enter a list: [1, 2, 4]

# Similarities to strings: indexing, slicing, looping
len(L)

if 2 in L:
    print('This list contains the number 2')
if 10 not in L:
    print('This list does not contain the number 10')


for i in range(len(L)):
    print(L[i])

for item in L:
    print (item)

# Built-in functions: len, sum, max, min
average = sum(L)/len(L)
min(L)
max(L)

# List methods: append, sort, count, index, reverse, remove, pop, insert. String methods do not change the original string but list methods DO change the original list.

# Write a program that generates a list L of 50 random numbers between 1 and 100:
from random import randint
x = randint(1, 100)
L = []
for i in range(50):
    L.append(x)
print(L)



# Count how many items in a list L are greater than 50:
count = 0
for item in L:
    if item > 50:
        count += 1
print (count)

# Given a list L that contains a number between 1 and 100, create a new list whose first element is how many ones are in L, whose second element is how many twos are in L, etc
L = [33, 12, 2, 67, 22,8, 99, 100, 1, 3,55, 6,7, 92]

new_L = []

for x in range(101):
    if x in L:
        new_L.append(L.count(x))
print(new_L)

# Print out the 2 largest and 2 smallest elements of a list called scores:
scores = [5, 6, 8, 7, 10, 10, 2, 4, 5, 5, 6]
scores.sort()
new_scores = []
for i in range(len(scores)):
	if (scores[i] in scores) and (scores[i] not in new_scores):
		new_scores.append(scores[i])
print('Two smallest scores are: {} and {}'.format(new_scores[0], new_scores[1])
print('Two largest scores are: {} and {}'.format(new_scores[-1], new_scores[-2])

# Quiz simple game:

num_right = 0

print('What is the capital of France?', end = ' ')
guess = inpu()
if guess.lower() == 'paris':
      print('Correct!')
      num_right += 1
else:
    print('Wrong, the answer is Paris')
print('You have', num_right, 'out of 1 right')

print('Which state has only one neighbor?', end = ' ')
guess = input()
if guess.lower() == 'maine':
    print('Correct!')
    num_right += 1
else:
    print('Wrong. The answer is Maine.')
print('You have', num_right, 'out of 2 right.')

    
# This game can be simplified with lists and loops:
question = ['What is the capital of France?',
            'Which state has only one neighbor?']
answer = ['Paris', 'Maine']

num_right = 0
for i in range(len(questions)):
    guess = input(question[i]):
        if guess.lower == answer[i].lower():
            print('Correct')
            num_right += 1
        else:
            print('Wrong. The answer is', answer[i])
        print('You have', num_right, 'out of', i + 1, 'right')

# Roll dice game:
dice_outcome = [1,2,3,4,5, 6]


# choice(L): picks a random item from L
from random import choice
names = ['Anna', 'Bob', 'Carl', 'Danny']
current_player = choice(name)

# sample(L, n): picks a group of n random items from L
from random import sample
team = sample(names, 2)

# shuffle(L): shuffles the items of L
from random import shuffle
players = ['Linh', 'Simon', 'QA', 'Tiff', 'Toan', 'Trang']
shuffle(players)
for player in players:
    print(player, 'it is your turn.')

# Split: Returns a list of the words of a string. The method assumes that words are separated by whitespace, which can be either spaces, tabs, or newline characters


# List comprehensions
L = [i for i in range(5)]

L = [[i, j] for i in range(2) for j in range(2)]

[[i,j] for i in range(4) for j in range(i)]

## Write a program that generates a list L of 50 random numbers between 1 and 100:
L = [randint(1,100) for i in range(50)]

## Replace each element in a list L with its square:
L = [i**2 for i in L]

## Count how many items in a list L are greater than 50
len([i for i in L if i>50])





