import random

# global variables - they are all intentially mutable
score_dict = {
    "total_score" : 0,
    "round_score" : 0,
}



current_round = 1

active_dice = []
saved_dice = []

def start_game():
    start_game_prompt = input('Are you ready to start a game of greed? (y/n)')
    
    if start_game_prompt == 'y':
        print('Here are your starting dice: ')
        # dice roll function is called after this in the call stack below

    elif start_game_prompt == 'n':
        global current_round
        current_round += 3
        print('you have exited the game')

# TODO: re-write this in such a way that it resets itself. Currently, the old remaining dice are added on, and the new roll is appended to that list. I am trying to figure out the best way to remove the old dice and only reroll a new hand
def roll_dice(dice):
    for i in range(6):             
        i = random.randint(1, 6) 
        active_dice.append(i)
    print(active_dice)
    return dice


def set_aside_dice():
    save_question = input('Would you live to save any dice?(y/n)')

    if save_question == 'y':
        print("""
Which dice do you wish to set aside any of these dice for scoring? 
Please separate your numbers with a space
        """)
        saved_dice = [int(n) for n in input().split(' ')]

        for i in saved_dice:
            active_dice.remove(i)
        print(f'These are the dice you saved: {saved_dice}')
        print(f'These are the dice you have remaining: {active_dice}')

    elif save_question == 'n':
        # breaks out of the game - currently here so I can playtest
        global current_round
        current_round += 3



# def determine_score(vals):
#     print(f'these are the number of ones: {saved_dice}')
#     if saved_dice.count(1) == 1:
#         score_dict["round_score"] += (saved_dice.count(1) * 100)

#     elif saved_dice.count(1) == 2:
#         score_dict["round_score"] += ((saved_dice.count(1) * 2) * 100)


#     print(f'Your score for this round: {score_dict["round_score"]}')
#     return vals

def determine_score(dice_values):
    dice_summary = {
        1: dice_values.count(1),
        2: dice_values.count(2),
        3: dice_values.count(3),
        4: dice_values.count(4),
        5: dice_values.count(5),
        6: dice_values.count(6),
    }

    pair_counter = 0
    is_a_straight = True

    for value, count in dice_summary.items():
        if count != 1:
            is_a_straight = False
        if count == 2:
            pair_counter += 1
    
    if is_a_straight:
        return 1500
    
    score = 0
    score += dice_summary[1] * 100
    score += dice_summary[5] * 50

    if pair_counter == 3:
        score = 1000
    
    return score


def play_round():
    roll_dice(active_dice)
    set_aside_dice()
    determine_score(score_dict["total_score"])
    # when user is done picking dice:
        # calculate score for the round
        # give option to:
            # re-roll remaining dice
                # if re-rolled and no score, zero out score for the round
            # bank score and start a new round with 6 dice
                # add banked score to total score
                



# This initiates the game, and allows the tests to accept input
if __name__ == "__main__":
    start_game()
    while current_round <= 3:   
        play_round()
