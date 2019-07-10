from game_of_greed import determine_score
from game_of_greed import roll_dice

def test_zilch():
    expected = 0
    actual =  determine_score([2, 3, 4, 6])
    assert expected == actual

def test_ones():
    assert determine_score([1]) == 100
    assert determine_score([1] * 2) == 200
    assert determine_score([1] * 3) == 1000
    assert determine_score([1] * 4) == 2000
    assert determine_score([1] * 5) == 3000
    assert determine_score([1] * 6) == 4000

    
def test_twos():
    assert determine_score([2] * 3) == 200
    assert determine_score([2] * 4) == 400
    assert determine_score([2] * 5) == 800
    assert determine_score([2] * 6) == 1600
    
def test_threes():
    assert determine_score([3] * 3) == 300
    assert determine_score([3] * 4) == 600
    assert determine_score([3] * 5) == 1200
    assert determine_score([3] * 6) == 2400

def test_fours():
    assert determine_score([4] * 3) == 400
    assert determine_score([4] * 4) == 800
    assert determine_score([4] * 5) == 1600
    assert determine_score([4] * 6) == 3200

def test_fives():
    assert determine_score([5]) == 50
    assert determine_score([5] * 2) == 100
    assert determine_score([5] * 3) == 500
    assert determine_score([5] * 4) == 1000
    assert determine_score([5] * 5) == 2000
    assert determine_score([5] * 6) == 4000

def test_sixes():
    assert determine_score([6] * 3) == 600
    assert determine_score([6] * 4) == 1200
    assert determine_score([6] * 5) == 2400
    assert determine_score([6] * 6) == 4800

def test_straight():
    assert determine_score([1, 2, 3, 4, 5, 6]) == 1500
    
# tests I am unsure how I want to tackle tonight:
    # test_three_pairs()
    # test_leftover_ones()
    # test_leftover_fives()
    # test_two_trios()


def test_roll_dice():
    # not sure how to set this up
    # I need it to check that the length of the active dice list <= 6 and that none of their values are higher than 6
    expected = ['this is here for me to fill in later']
    actual = ['so is this']
    assert expected == actual