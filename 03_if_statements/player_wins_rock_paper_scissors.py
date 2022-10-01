from reference_data import *


def player_wins_rock_paper_scissors(player_input: str, computer_input: str) -> str:
    if player_input != ROCK and player_input != PAPER and player_input != SCISSORS:
        raise NameError('I do not understand the command: ' + player_input)

    if player_input == computer_input:
        return DRAW

    if player_input == ROCK:
        if computer_input == SCISSORS:
            return WIN
        else:
            return LOSS
    if player_input == PAPER:
        if computer_input == ROCK:
            return WIN
        else:
            return LOSS
    if player_input == SCISSORS:
        if computer_input == PAPER:
            return WIN
        else:
            return LOSS


def test():
    assert player_wins_rock_paper_scissors(ROCK, ROCK) == DRAW
    assert player_wins_rock_paper_scissors(ROCK, SCISSORS) == WIN
    assert player_wins_rock_paper_scissors(SCISSORS, ROCK) == LOSS
    assert player_wins_rock_paper_scissors(PAPER, PAPER) == DRAW
    assert player_wins_rock_paper_scissors(PAPER, ROCK) == WIN
    assert player_wins_rock_paper_scissors(ROCK, PAPER) == LOSS
    assert player_wins_rock_paper_scissors(SCISSORS, SCISSORS) == DRAW
    assert player_wins_rock_paper_scissors(SCISSORS, PAPER) == WIN
    assert player_wins_rock_paper_scissors(PAPER, SCISSORS) == LOSS
    try:
        player_wins_rock_paper_scissors('bad input', SCISSORS)  # should complain if given bad input
        assert False
    except NameError:
        assert True
    print('All tests passed!')


test()
