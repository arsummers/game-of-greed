import random
from rule_set import RuleSet

# global variables 
total_score = 0
round_score = 0
score = 0

# rule_set = RuleSet()

current_round = 1

active_dice = []
saved_dice = []
round_saved_for_scoring = []
total_saved_for_scoring = []

def start_game():
    start_game_prompt = input('Are you ready to start a game of greed? (Y/N)')
    
    if start_game_prompt == 'Y':
        print('Here are your starting dice: ')
        # dice roll function is called after this in the call stack below

    elif start_game_prompt == 'N':
        global current_round
        current_round += 3
        print('you have exited the game')

        
def start_dice(dice):
    for i in range(6):             
        i = random.randint(1, 6) 
        active_dice.append(i)
    print(active_dice)
    return dice


def roll_dice(dice):
    global active_dice
    # resets the active dice pool to keep it from getting larger than 6 dice
    active_dice = []            

    for i in range(len(dice)): 
        i = random.randint(1, 6)        
        active_dice.append(i)
    print(active_dice)
    return dice




# TODO: game should put ruleset into a class that is used within the game to assign points. I think this'll be different/separate from the determine_score function, but I will have to make them interact with each other. My class will have the rules, and the things needed to pass the test. Maybe the function will live in here too?


# TODO: find a way to work the array of round_saved_dice into the scoring function

# def determine_score(dice_values):
#     global score
#     dice_summary = {
#         1: dice_values.count(1),
#         2: dice_values.count(2),
#         3: dice_values.count(3),
#         4: dice_values.count(4),
#         5: dice_values.count(5),
#         6: dice_values.count(6),
#     }

#     pair_counter = 0
#     is_a_straight = True

#     for value, count in dice_summary.items():
#         if count != 1:
#             is_a_straight = False
#         if count == 2:
#             pair_counter += 1    
    
#     if is_a_straight:
#         return rule_set.get_score('3 pairs')

#     score = 0
    
#     score += dice_summary[1] * 100
#     score += dice_summary[5] * 50

#     if pair_counter == 3:
#         score = 1000

#     # TODO: learn the syntax to make this work - should pass remaining ones tests when out of pseudo code
#     # to test ones greater than count 3:
#         # if count of 1 >= 3:
#             # score = 1000
#             # repeat for each die past 3
#             # score += 1000

#     # to test non-one rolls of 3 or more:
#         # if count of that number >= 3:
#             # score = num * 100
#             # repeat for each die past 3
#             # score += score
    
#     return score



def set_aside_dice():
    global active_dice
    global round_saved_for_scoring

    save_question = input('Would you live to save any dice?(Y/N)')

    if save_question == 'Y':
        print("""
Which dice do you wish to set aside any of these dice for scoring? 
Please separate your numbers with a space
        """)
        saved_dice = [int(n) for n in input().split(' ')]

        # saved dice is getting appended as a list
        # will need to have it appended as plain integers, and reset when I reroll

        for i in saved_dice:
            active_dice.remove(i)
        
        for num in saved_dice:
            round_saved_for_scoring.append(num)

        print(f'These are the dice you saved: {round_saved_for_scoring}')
        print(f'These are the dice you have remaining. They have been rerolled for you:')

    elif save_question == 'N':
        # breaks out of the game - currently set to 3 so I can playtest easily
        start_new_round_prompt = input('Would you like to REROLL with 6 new dice and start a new round, or would you like to QUIT the game?')

        if start_new_round_prompt == 'QUIT':
            global current_round
            current_round += 3
        elif start_new_round_prompt == 'REROLL':
            round_saved_for_scoring = []
            active_dice = []
            start_dice(active_dice)
            set_aside_dice()
            current_round += 1



def play_round():
    set_aside_dice()
    roll_dice(active_dice)
    # determine_score(round_saved_for_scoring) 
    # TODO: see below
    # when user is done picking dice:
        # calculate score for the round
        # give option to:
            # re-roll remaining dice- DONE
                # if re-rolled and no score, zero out score for the round
            # bank score and start a new round with 6 dice
                # add banked score to total score
                   
# This initiates the game, and allows the tests to accept input
if __name__ == "__main__":
    start_game()
    start_dice(active_dice) 
    while current_round <= 3:  
        play_round()


# after main game, print scores to scores.txt
def read_file(path):
    try:
        with open(path) as file:
            contents = file.read()

        contents += f'Scores: {score} - has been read'

        with open('scores.txt', 'w') as outputfile:
            outputfile.write(contents)

        print('write completed')

    finally:
        print('Thanks for playing!')

try:
    read_file('house_rules.txt')

except FileNotFoundError as error:
    print('handled error: ')
    print(error)

except:
    print('it was a different error')