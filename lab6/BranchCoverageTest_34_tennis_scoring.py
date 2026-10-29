
import pytest
from tennis_scoring import game_score, set_winner, match_status


# Game score tests
def test_negative_points():
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)


def test_regular_game_scores():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 2) == "15-30"
    assert game_score(3, 2) == "40-30"


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_winner_from_deuce():
    assert game_score(5, 3) == "game A"
    assert game_score(3, 5) == "game B"


def test_advantage():
    assert game_score(4, 3) == "advantage A"
    assert game_score(3, 4) == "advantage B"


def test_game_winner_before_deuce():
    assert game_score(4, 0) == "game A"
    assert game_score(0, 4) == "game B"


# Set winner tests
def test_set_winner_by_two_game_lead():
    assert set_winner(6, 4) == "A"
    assert set_winner(4, 6) == "B"


def test_set_winner_by_tiebreak_score():
    assert set_winner(7, 6) == "A"
    assert set_winner(6, 7) == "B"


def test_set_undecided():
    assert set_winner(3, 2) is None


# Match status tests
def test_match_status():
    assert match_status(2, 0, 3) == "A wins"
    assert match_status(0, 2, 3) == "B wins"
    assert match_status(1, 1, 3) == "decider"
    assert match_status(1, 0, 3) == "in progress"
