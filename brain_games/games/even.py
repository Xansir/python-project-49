import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    question = random.randint(0, 40)
    if is_even(question):
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct


def is_even(question):
    return True if question % 2 == 0 else False
