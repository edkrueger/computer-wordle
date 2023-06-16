import os

GREEN = 2
YELLOW = 1
GRAY = 0


def get_wordle_words():
    with open(os.path.join("computer_wordle", "possible_wordle_words.txt")) as f:
        wordle_words = set()
        for line in f:
            wordle_words |= {line.strip()}
    return wordle_words


WORDLE_WORDS = get_wordle_words()


def _check(target_word, guess_word):
    result = 5 * [GRAY]

    target_list = list(target_word)
    guess_list = list(guess_word)

    for i, (target_char, guess_char) in enumerate(zip(target_list, guess_list)):
        if target_char == guess_char:
            result[i] = GREEN
            target_list[i] = None
            guess_list[i] = None

    for i, guess_char in enumerate(guess_list):
        if guess_char == None:
            continue
        for j, target_char in enumerate(target_list):
            if target_char == None:
                continue
            if guess_char == target_char:
                result[i] = YELLOW
                target_list[j] = None
                break
    return result


def check(target_word, guess_word):
    if not guess_word in WORDLE_WORDS:
        raise ValueError(f"{guess_word=} is not valid!")
    return _check(target_word=target_word, guess_word=guess_word)
