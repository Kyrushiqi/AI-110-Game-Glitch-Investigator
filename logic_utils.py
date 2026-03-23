# FIX: Transfered app.py's 4 functions to logic_utils.py using Copilot. 
# Updated imports in app.py and tests/test_game_logic.py accordingly.

# FIX: get_range_for_difficulty now returns (1, 20) for "Easy", (1, 50) for "Normal", and (1, 100) for "Hard". 
# The previous version's ranges for each difficulty level doesn't match their corresponding difficulty level. 
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Fixed the hint directions in check_guess. Too High => Go LOWER!, Too Low => Go HIGHER!. 
# The previous version's hint directions were reversed.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        secret_val = int(secret)
    except Exception:
        secret_val = secret

    if guess == secret_val:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret_val:
            return "Too High", "📈 Go LOWER!"
        return "Too Low", "📉 Go HIGHER!"
    except TypeError:
        # Fallback for non-numeric comparison
        if str(guess) == str(secret):
            return "Win", "🎉 Correct!"
        if str(guess) > str(secret):
            return "Too High", "📈 Go LOWER!"
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
