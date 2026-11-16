def _parse_non_negative_integers(text, separator):
    if not isinstance(text, str):
        return None

    fields = [field.strip() for field in text.split(separator)]
    if not fields or any(not field or not field.isascii() or not field.isdecimal() for field in fields):
        return None

    try:
        return [int(field) for field in fields]
    except (ValueError, OverflowError):
        return None


def parse_score(text):
    scores = _parse_non_negative_integers(text, '-')
    if scores is None or len(scores) != 2:
        return None
    return scores[0], scores[1]


def game_lead(text):
    if not isinstance(text, str):
        return None

    parts = text.split('-')
    if len(parts) != 2:
        return None

    first, second = (part.strip() for part in parts)
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    if first not in points or second not in points:
        return None
    return points[first] - points[second]


def set_spread(games_csv):
    games = _parse_non_negative_integers(games_csv, ',')
    if games is None:
        return None
    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    if result is None:
        print("Invalid score. Enter two non-negative whole numbers separated by '-'.")
    else:
        print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    if result is None:
        print("Invalid game score. Use 0, 15, 30, or 40 on each side.")
    else:
        print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    if result is None:
        print("Invalid set scores. Enter one or more non-negative whole numbers separated by commas.")
    else:
        print("Spread:", result)


if __name__ == "__main__":
    main()
