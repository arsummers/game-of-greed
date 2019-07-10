# __if name__ == "__main__"

from game_of_greed import determine_score
from game_of_greed import roll_dice

def test_1():
    # expected
    # actual
    assert determine_score([1]) == 100



def test_roll_dice():
    # not sure how to set this up
    # I need it to check that the length of the active dice list <= 6 and that none of their values are higher than 6
    expected = ['this is here for me to fill in later']
    actual = ['so is this']
    assert expected == actual