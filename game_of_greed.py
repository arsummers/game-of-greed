
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

total_score = 0
round_score = 0
current_round = 1

max_dice = []
active_dice = []
saved_dice = []

def randomize_dice(dice):
    for i in range(6):
        i = random.randint(1, 6) 
        max_dice.append(i)
        active_dice.append(i)

# this allows me to start with a random set of dice to pick through
randomize_dice(max_dice)

# sorts through lists of dice. Lets user pick one die at a time, and removes it from the available pool of dice. 

while True:
    if len(active_dice) >= 1:
        dice_prompt = f"""What do you want to save?{active_dice}"""
    else:
        dice_prompt = f"""What do you want to save?{max_dice}"""

    # this bit is commented out until I can test it
    # save_these = input(dice_prompt)
    # saved_dice = []

    # for char in save_these:
    #     saved_dice.append(int(char))
    # print(saved_dice)

    save_these = int(input(dice_prompt))

    if save_these in max_dice:

        saved_dice.append(save_these)
        active_dice.remove(save_these)

        print(f'these are the dice you have banked: {saved_dice}')
        print(f'these are your remaining dice for the round: {active_dice}')

    if len(active_dice) == 0:
        print(f'you are out of dice. Try again. End of round {current_round}')
        current_round += 1
        print(dice_prompt)
        saved_dice = []
        max_dice = []
        randomize_dice(max_dice)
        print(max_dice)
        continue



