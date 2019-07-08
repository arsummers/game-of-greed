
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
current_round = 0

max_dice = []
saved_dice = []
active_dice = []

for i in range(6):
    i = random.randint(1, 6) 
    max_dice.append(i)
    active_dice.append(i)

# prints the array of dice with random numbers between 1 and 6
# do not need to shuffle, since randomly generating numbers for them takes care of that





while True:
    dice_prompt = f"""What do you want to save?{active_dice}"""
    save_these = int(input(dice_prompt))

    if save_these not in max_dice:
        print('that number doesn\'t exist here')
        break

    if save_these in max_dice:

        saved_dice.append(save_these)
        active_dice.remove(save_these)

        print(f'these are the dice you have banked: {saved_dice}')
        print(f'these are your remaining dice for the round: {active_dice}')

    if len(active_dice) == 0:
        print('you are out of dice. Try again')
        print(dice_prompt)
        print(max_dice)
        continue


# while len(active_dice) != 0:
#      print('enter your score for this round:')
#         entered_score = int(input())

#         round_score += entered_score
#         total_score += entered_score
#         print(f'this is your total score for the round: {round_score}')
#         break


