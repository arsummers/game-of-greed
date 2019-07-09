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
    dice_prompt = f"""What do you want to save?{active_dice}"""

    save_these = int(input(dice_prompt))


    if save_these in max_dice:

        saved_dice.append(save_these)
        active_dice.remove(save_these)

        print(f'these are the dice you have banked: {saved_dice}')
        print(f'these are your remaining dice for the round: {active_dice}')

    reroll_prompt = 'If you would like to reroll the remaining dice, enter Y. If you would like to continue picking dice, enter C.'
    reroll_input = input(reroll_prompt)

    if reroll_input == 'Y':
            randomize_dice(active_dice)

    if len(active_dice) <= 3:
        add_to_score_prompt = "Would you like to enter your score for this roll, and roll remaining dice? Y/N. "
        add_to_score_input = input(add_to_score_prompt)


        if add_to_score_input == 'Y':
            round_score_prompt = "Enter your score"
            round_score_input = int(input(round_score_prompt))
            round_score += round_score_input
            print(f'Your current score for this round: {round_score}')

        elif add_to_score_input == 'N':
            print('this will reroll all the dice')

    if len(active_dice) == 0 and current_round < 3:
        print(f'you are out of dice. Try again. End of round {current_round}')
        current_round += 1
        total_score += round_score
        round_score = 0
        saved_dice = []
        max_dice = []
        randomize_dice(max_dice)
        continue
    if total_score >= 10000:
        print(f'this is your final score: {total_score}. It took you {current_round} rounds to get here')

