import pytest
from computer_wordle.wordle import GREEN, YELLOW, GRAY, _check, check


@pytest.mark.parametrize(
    "target_word, guess_word, expected_result",
    [
        ("fluff", "aaaaa", [GRAY, GRAY, GRAY, GRAY, GRAY]),
        ("fluff", "faaaa", [GREEN, GRAY, GRAY, GRAY, GRAY]),
        ("fluff", "afaaa", [GRAY, YELLOW, GRAY, GRAY, GRAY]),
        ("fluff", "affaa", [GRAY, YELLOW, YELLOW, GRAY, GRAY]),
        ("fluff", "ffaaa", [GREEN, YELLOW, GRAY, GRAY, GRAY]),
        ("fluff", "fffaa", [GREEN, YELLOW, YELLOW, GRAY, GRAY]),
        ("fluff", "afaaf", [GRAY, YELLOW, GRAY, GRAY, GREEN]),
        ("fluff", "affaf", [GRAY, YELLOW, YELLOW, GRAY, GREEN]),
        ("fluff", "faaaf", [GREEN, GRAY, GRAY, GRAY, GREEN]),
        ("fluff", "fafaf", [GREEN, GRAY, YELLOW, GRAY, GREEN]),
        ("fluff", "aafaa", [GRAY, GRAY, YELLOW, GRAY, GRAY]),
    ],
)
def test__check(target_word, guess_word, expected_result):
    result = _check(target_word=target_word, guess_word=guess_word)

    assert result == expected_result


@pytest.mark.parametrize(
    "target_word, guess_word, expected_result",
    [
        ("fluff", "world", [GRAY, GRAY, GRAY, YELLOW, GRAY]),
        ("fluff", "ficin", [GREEN, GRAY, GRAY, GRAY, GRAY]),
        ("fluff", "mafic", [GRAY, GRAY, YELLOW, GRAY, GRAY]),
    ],
)
def test_check(target_word, guess_word, expected_result):
    result = check(target_word=target_word, guess_word=guess_word)

    assert result == expected_result


def test_check_on_invalid_guess():
    target_word = "fluff"
    guess_word = "aaaaa"
    with pytest.raises(ValueError):
        check(target_word=target_word, guess_word=guess_word)
