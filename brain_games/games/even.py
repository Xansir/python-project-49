import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    question = random.randint(0, 40)
    if question % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct