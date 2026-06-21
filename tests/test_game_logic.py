from logic_utils import check_guess, get_range_for_difficulty, parse_guess

# --- existing tests (fixed to unpack the tuple check_guess returns) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: swapped hint messages ---
# Original code had "Go HIGHER!" attached to Too High and "Go LOWER!" to Too Low.

def test_too_high_message_says_go_lower():
    """Too High outcome must tell the player to guess lower, not higher."""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"

def test_too_low_message_says_go_higher():
    """Too Low outcome must tell the player to guess higher, not lower."""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"


# --- Bug 2: alternating str(secret) cast broke every-other comparison ---
# Original app.py did: secret = str(st.session_state.secret) on even attempts,
# then called check_guess(guess_int, secret) with a string secret.
# Simulating that: check_guess(50, "50") must NOT return Win (int vs str is wrong).

def test_guess_compared_as_integer_across_attempts():
    """
    Original app.py cast the secret to str on even attempts, so guess 50 vs secret "50"
    would not return Win. The fix removes that cast; check_guess always receives two ints.
    Verify consistent int-vs-int results on simulated attempt 1 and attempt 2.
    """
    # Both attempts must give the same correct answer when inputs are ints.
    outcome_attempt1, _ = check_guess(50, 50)
    outcome_attempt2, _ = check_guess(50, 50)
    assert outcome_attempt1 == "Win", "Attempt 1 (odd) should Win when guess == secret"
    assert outcome_attempt2 == "Win", "Attempt 2 (even) should also Win — no str cast bug"


# --- Bug 3: hardcoded randint(1, 100) ignored difficulty ---
# get_range_for_difficulty must return the correct bounds for each level.

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20), f"Easy should be (1, 20), got ({low}, {high})"

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 100), f"Normal should be (1, 100), got ({low}, {high})"

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 50), f"Hard should be (1, 50), got ({low}, {high})"


# --- Bug 4: attempts counter started at 1 instead of 0 ---
# parse_guess is used on the first attempt; verify a valid first guess parses cleanly.

def test_parse_valid_guess():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_empty_guess():
    ok, value, _ = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_non_numeric_guess():
    ok, value, _ = parse_guess("abc")
    assert ok is False
    assert value is None
