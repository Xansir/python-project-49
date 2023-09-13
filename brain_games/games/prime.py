import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    question = random.randint(2, 100)
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            correct = 'no'
            break
        else:
            correct = 'yes'
    return question, correct
