from game_of_greed import determine_score
from game_of_greed import roll_dice
from game_of_greed import RuleSet

def test_zilch():
    expected = 0
    actual =  determine_score([2, 3, 4, 6])
    assert expected == actual

# TESTING ONES

def test_single_one():
    assert determine_score([1]) == 100

def test_two_ones():
    assert determine_score([1, 1]) == 200

# TODO: GET PASSING
def test_three_through_six_ones():
    assert determine_score([1] * 3) == 1000
    assert determine_score([1] * 4) == 2000
    assert determine_score([1] * 5) == 3000
    assert determine_score([1] * 6) == 4000

def test_out_of_order():
    assert determine_score([3, 1]) == 100

# TESTING TWOS

# TODO: GET PASSING
def test_twos():
    assert determine_score([2] * 3) == 200
    assert determine_score([2] * 4) == 400
    assert determine_score([2] * 5) == 800
    assert determine_score([2] * 6) == 1600

def test_single_two():
    assert determine_score([2]) == 0
    
# TESTING THREES

# TODO: GET PASSING
def test_threes():
    assert determine_score([3] * 3) == 300
    assert determine_score([3] * 4) == 600
    assert determine_score([3] * 5) == 1200
    assert determine_score([3] * 6) == 2400

# TESTING FOURS

# TODO: GET PASSING
def test_fours():
    assert determine_score([4] * 3) == 400
    assert determine_score([4] * 4) == 800
    assert determine_score([4] * 5) == 1600
    assert determine_score([4] * 6) == 3200

# TESTING FIVES

# TODO: GET PASSING
def test_fives():
    assert determine_score([5] * 2) == 100
    assert determine_score([5] * 3) == 500
    assert determine_score([5] * 4) == 1000
    assert determine_score([5] * 5) == 2000
    assert determine_score([5] * 6) == 4000

def test_single_five():
    assert determine_score([5]) == 50

def test_multiple_fives():
    assert determine_score([5] * 2) == 100
    


# TESTING SIXES

# TODO: GET PASSING
def test_sixes():
    assert determine_score([6] * 3) == 600
    assert determine_score([6] * 4) == 1200
    assert determine_score([6] * 5) == 2400
    assert determine_score([6] * 6) == 4800

# TESTING STRAIGHT
def test_straight():
    assert determine_score([1,6,2,5,3,4]) == 1500

# TESTING THREE PAIRS
def test_three_pairs():
    assert determine_score([2,2,3,3,4,4]) == 1000

def test_three_pairs_with_ones_and_fives():
    assert determine_score([1,1,3,3,5,5]) == 1000

# TESTING LEFTOVER ONES
# TODO: WRITE TEST

# TESTING LEFTOVER FIVES
# TODO: WRITE TEST

# TESTING TWO TRIOS  
# TODO: GET PASSING, REWRITE AS NEEDED
def test_two_trios():
    assert determine_score([2,2,2,4,4,4]) == 700


def test_roll_dice():
    # not sure how to set this up
    # I need it to check that the length of the active dice list <= 6 and that none of their values are higher than 6
    assert roll_dice

def test_rule_set():
    assert RuleSet

# TODO: insert test_read_file(), unsure of syntax since it has an argument