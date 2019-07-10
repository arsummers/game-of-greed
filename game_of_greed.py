import random

def determine_score(vals):
    # between 1 and 6 values
    # test saved dice for scoring

    return None

total_score = 0
round_score = 0
current_round = 1

active_dice = []
saved_dice = []

def start_game():
    start_game_prompt = input('Are you ready to start a game of greed?')
    
    if start_game_prompt == 'Y':
        print('Here are your starting dice: ')
        # dice roll function is called after this in the call stack below

    elif start_game_prompt == 'N':
        print('you have exited the game')


def roll_dice(dice):
    for i in range(6):             
        i = random.randint(1, 6) 
        active_dice.append(i)
    print(active_dice)
    return dice

def set_aside_dice():
    print('Which dice do you wish to set aside any of these dice for scoring?')
    saved_dice = [int(n) for n in input().split(' ')]

    for i in saved_dice:
        active_dice.remove(i)
    print(f'These are the dice you saved: {saved_dice}')
    print(f'These are the dice you have remaining: {active_dice}')


# def current_active_dice():
#     # global active_dice
#     initial_dice = roll_dice(active_dice)

#     # This just keeps the list of active dice from getting too long, and resets it for future rolls
#     if len(active_dice) > 6:
#         # active_dice = []
#         next_dice = roll_dice(active_dice)
#         print(f'This is your next round: {next_dice}')

#     # These are the dice I want to work with
#     if len(initial_dice) <= 6:
#         print(active_dice)
    

# def save_from_roll():
#     save_from_roll_prompt = int(input('Which dice to you wish to save for scoring?'))

#     saved_dice_values = save_from_roll_prompt
#     print(f'These are the values of the saved dice: {saved_dice_values}')

#     # is this a subsection of the dice pool - going to need something other than in
#     if saved_dice_values in active_dice:
#         saved_dice.append(save_from_roll_prompt)
#         active_dice.remove(save_from_roll_prompt)
#         print(f'Here are the dice you banked: {saved_dice}')
#         print(f'Here are your remaining dice: {active_dice}')

#     elif saved_dice_values not in active_dice:
#         print('That was not a valid die. Don\'t be a cheater!')

# # TODO: find a good way to repeat this
# def save_these_dice_flow():
#     global current_round

#     while len(saved_dice) < 6:
#         save_decision_prompt = input('Do you want to save any of these dice?')

#         if save_decision_prompt == 'Y':
#             current_round += 1
#             save_from_roll()
#         if save_decision_prompt == 'N':
#             current_round += 1
#             print(f'The dice will now reroll. Start of round {current_round}')
#         # TODO: work on this bit - it isn't re-rendering as needed
#             save_from_roll()
#             save_decision_prompt = input('Do you want to save any of these dice?')
#             print('These are from line 70', active_dice)
#             # current_active_dice()
#             roll_dice(active_dice)       
#             continue



def play_round():
    roll_dice(active_dice)
    set_aside_dice()

    # let user pick dice
        # let user pick multiple dice at once
    # when user is done picking dice:
        # calculate score for the round
        # give option to:
            # re-roll remaining dice
                # if re-rolled and no score, zero out score for the round
            # bank score and start a new round with 6 dice
                # add banked score to total score



# should be in name == main thing

start_game()   
play_round()


# roll_dice(active_dice)  
# save_these_dice_flow()
# determine_score()

# pick dice to keep 

# TODO: select multiple dice at once. Successfully remove from active pool. Write tests for scoring





# while True:
#     dice_prompt = f"""What do you want to save?{active_dice}"""

#     save_these = int(input(dice_prompt))


#     if save_these in max_dice:

#         saved_dice.append(save_these)
#         active_dice.remove(save_these)

#         print(f'these are the dice you have banked: {saved_dice}')
#         print(f'these are your remaining dice for the round: {active_dice}')

#     reroll_prompt = 'If you would like to reroll the remaining dice, enter Y. If you would like to continue picking dice, enter C.'
#     reroll_input = input(reroll_prompt)

#     if reroll_input == 'Y':
#             roll_dice(active_dice)

#     if len(active_dice) <= 3:
#         add_to_score_prompt = "Would you like to enter your score for this roll, and roll remaining dice? Y/N. "
#         add_to_score_input = input(add_to_score_prompt)


#         if add_to_score_input == 'Y':
#             round_score_prompt = "Enter your score"
#             round_score_input = int(input(round_score_prompt))
#             round_score += round_score_input
#             print(f'Your current score for this round: {round_score}')

#         elif add_to_score_input == 'N':
#             print('this will reroll all the dice')

#     if len(active_dice) == 0 and current_round < 3:
#         print(f'you are out of dice. Try again. End of round {current_round}')
#         current_round += 1
#         total_score += round_score
#         round_score = 0
#         saved_dice = []
#         max_dice = []
#         randomize_dice(max_dice)
#         continue
#     if total_score >= 10000:
#         print(f'this is your final score: {total_score}. It took you {current_round} rounds to get here')
