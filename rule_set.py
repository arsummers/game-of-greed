class RuleSet:
    # TODO: make functions or method to get score
    # how storing scores, scoring, rules for scoring

    def __init__(self):
        pass

    rules_dict = {
        "straight": 1500,
        "three_pairs": 1000,
        "one_ones": 100,
        "two_oness": 200,
        "three_ones": 1000,
        "four_ones": 2000,
        "five_ones": 3000,
        "six_ones": 4000,
        "one_twos": 0,
        "two_twos": 0,
        "three_twos": 200,
        "four_twos": 400,
        "five_twos": 800,
        "six_twos": 1600,
        "one_threes": 0,
        "two_threes": 0,
        "three_threes": 300,
        "four_threes": 600,
        "five_threes": 1200,
        "six_threes": 2400,
        "one_fours": 0,
        "two_fours": 0,
        "three_fours": 400,
        "four_fours": 800,
        "five_fours": 1600,
        "six_fours": 3600,
        "one_fives": 50,
        "two_fives": 100,
        "three_fives": 500,
        "four_fives": 1000,
        "five_fives": 2000,
        "six_fives": 4000,
        "one_sixes": 0,
        "two_sixes": 0,
        "three_sixes": 600,
        "four_sixes": 1200,
        "five_sixes": 2400,
        "six_sixes": 4800,
    }


    def determine_score(self, dice_values):           

        dice_summary = {
                1: dice_values.count(1),
                2: dice_values.count(2),
                3: dice_values.count(3),
                4: dice_values.count(4),
                5: dice_values.count(5),
                6: dice_values.count(6),
            }

        score = 0
        pair_counter = 0
        is_a_straight = True

        for value, count in dice_summary.items():
            if count != 1:
                is_a_straight = False
            if count == 2:
                pair_counter += 1    
        
        if is_a_straight:
            return self.determine_score("straight")

        score += dice_summary[1] * 100
        score += dice_summary[5] * 50

        if pair_counter == 3:
            score = 1000

        # TODO: learn the syntax to make this work - should pass remaining ones tests when out of pseudo code
        # to test ones greater than count 3:
            # if count of 1 >= 3:
                # score = 1000
                # repeat for each die past 3
                # score += 1000

        # to test non-one rolls of 3 or more:
            # if count of that number >= 3:
                # score = num * 100
                # repeat for each die past 3
                # score += score
        
        return score