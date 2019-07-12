class RuleSet:
    # TODO: make functions or method to get score
    def get_score(self, roll_type):
        return 500

    # def determine_score(dice_values):
    # # global score
    # dice_summary = {
    #     1: dice_values.count(1),
    #     2: dice_values.count(2),
    #     3: dice_values.count(3),
    #     4: dice_values.count(4),
    #     5: dice_values.count(5),
    #     6: dice_values.count(6),
    # }

    # pair_counter = 0
    # is_a_straight = True

    # for value, count in dice_summary.items():
    #     if count != 1:
    #         is_a_straight = False
    #     if count == 2:
    #         pair_counter += 1    
    
    # if is_a_straight:
    #     return rule_set.get_score('3 pairs')

    # score = 0
    
    # score += dice_summary[1] * 100
    # score += dice_summary[5] * 50

    # if pair_counter == 3:
    #     score = 1000

    # # TODO: learn the syntax to make this work - should pass remaining ones tests when out of pseudo code
    # # to test ones greater than count 3:
    #     # if count of 1 >= 3:
    #         # score = 1000
    #         # repeat for each die past 3
    #         # score += 1000

    # # to test non-one rolls of 3 or more:
    #     # if count of that number >= 3:
    #         # score = num * 100
    #         # repeat for each die past 3
    #         # score += score
    
    # return score