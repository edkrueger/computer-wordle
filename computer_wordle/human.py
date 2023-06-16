import random

from wordle import WORDLE_WORDS, GRAY, YELLOW, GREEN, check

TRANSLATION = {
    GRAY: "⬜",
    YELLOW: "🟨",
    GREEN: "🟩",
}


def translate_check_result(result):
    return "".join(TRANSLATION[e] for e in result)


def human_play(target_word=None):
    if not target_word:
        target_word = random.choice(list(WORDLE_WORDS))
    for round in range(1, 6):
        while True:
            try:
                guess_word = input("Enter your guess!\n").lower()
                result = check(target_word=target_word, guess_word=guess_word)
                print(translate_check_result(result))
                break
            except ValueError as e:
                print(e)
                print("Try again!")
        if guess_word == target_word:
            print(f"You win! {round=}")
    print(f"You lose! {target_word=}")


if __name__ == "__main__":
    human_play()
