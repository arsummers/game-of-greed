import random
from rule_set import RuleSet

# global variables 
total_score = 0
round_score = 0
score = 0

rule_set = RuleSet()

current_round = 0

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

def set_aside_dice():
    global active_dice
    global round_score
    global total_score
    global current_round
    global round_saved_for_scoring
    
    current_round += 1
    save_question = input('Would you live to save any dice?(Y/N)')

    if save_question == 'Y':
        print("""
Which dice do you wish to set aside any of these dice for scoring? 
Please separate your numbers with a space
        """)
        saved_dice = [int(n) for n in input().split(' ')]

        current_score_for_roll = rule_set.determine_score(saved_dice)
        round_score += current_score_for_roll
        print(f'CURRENT SCORE FOR THIS ROLL: {round_score}')
        print(f'TOTAL SCORE FOR THIS GAME: {total_score}')

        for i in saved_dice:
            active_dice.remove(i)
        
        for num in saved_dice:
            round_saved_for_scoring.append(num)

        print(f'These are the dice you saved: {round_saved_for_scoring}')
        print(f'These are the dice you have remaining. They have been rerolled for you:')

    elif save_question == 'N':

        start_new_round_prompt = input('Would you like to bank your score for this round and REROLL with 6 new dice, or would you like to QUIT the game and see your final score?')

       
        if start_new_round_prompt == 'REROLL':
            round_saved_for_scoring = []
            active_dice = []
            total_score += round_score
            round_score = 0
            print(f'Beginning of round {current_round}')
            start_dice(active_dice)
            set_aside_dice()
        elif start_new_round_prompt == 'QUIT':
# breaks out of the game - currently set to 3 so I can playtest easily
            total_score += round_score
            current_round += 3


def play_round():   
    set_aside_dice()
    roll_dice(active_dice)
    rule_set.determine_score(round_saved_for_scoring) 
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
        print(f'Thanks for playing! Your final score was {total_score} after {current_round} rounds')

try:
    read_file('house_rules.txt')

except FileNotFoundError as error:
    print('handled error: ')
    print(error)

except:
    print('it was a different error')