import random
min = 1
max = 6

roll_again = "yes"
while roll_again == 'yes':
    print ("Rolling the dice...")
    print ("The values are...")
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = input("Roll the dices again?")

print('Do you want to play a game? Y/N')
answer = input()
if answer == 'Y':
    roll_dice = random.randint(1, 6)
if answer == 'N':
    print('Okay bummer.')
    
