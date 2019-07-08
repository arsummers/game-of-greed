
    # interactive counter
#The dice output will be random - between 1 and 6

# Set aside dice after each roll
    # when the input number matches the number of the dice, take away that many of that number from the main dice pool
    # re-render the remaining number of dice, repeat as needed

# allow user to enter their score
    # see demo

# let user bank current score
    # score will += input
    # when banked, reset dice back to 6

# have a counter for rounds
import random

max_dice = []
current_score = 0
current_round = 0

for i in range(6):
    i = random.randint(1, 6) 
    max_dice.append(i)

# prints the array of dice with random numbers between 1 and 6
# do not need to shuffle, since randomly generating numbers for them takes care of that
print(max_dice)


