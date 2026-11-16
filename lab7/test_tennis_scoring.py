from hypothesis import given, settings, strategies as st

from tennis_scoring import parse_score, game_lead, set_spread


arbitrary_inputs = st.one_of(st.text(), st.none())


@settings(max_examples=200)
@given(arbitrary_inputs)
def test_parse_score_handles_arbitrary_input(value):
    parse_score(value)


@settings(max_examples=200)
@given(arbitrary_inputs)
def test_game_lead_handles_arbitrary_input(value):
    game_lead(value)


@settings(max_examples=200)
@given(arbitrary_inputs)
def test_set_spread_handles_arbitrary_input(value):
    set_spread(value)


@given(
    st.integers(min_value=0, max_value=1_000_000),
    st.integers(min_value=0, max_value=1_000_000),
)
def test_parse_score_returns_both_valid_scores(first, second):
    assert parse_score(f"{first}-{second}") == (first, second)


@given(
    st.sampled_from(["0", "15", "30", "40"]),
    st.sampled_from(["0", "15", "30", "40"]),
)
def test_game_lead_matches_tennis_point_values(first, second):
    values = {"0": 0, "15": 1, "30": 2, "40": 3}
    assert game_lead(f"{first}-{second}") == values[first] - values[second]


@given(st.lists(st.integers(min_value=0, max_value=1_000_000), min_size=1, max_size=20))
def test_set_spread_matches_list_range(games):
    csv_text = ",".join(str(game) for game in games)
    assert set_spread(csv_text) == max(games) - min(games)


def test_parse_score_rejects_invalid_input():
    for value in [None, "", "1", "1-2-3", "-1-2", "1-x"]:
        assert parse_score(value) is None


def test_game_lead_rejects_invalid_input():
    for value in [None, "", "40", "40-30-15", "10-40", "40-x"]:
        assert game_lead(value) is None


def test_set_spread_rejects_invalid_input():
    for value in [None, "", "6,,7", "-1,4", "6,4, ", "one,two"]:
        assert set_spread(value) is None
