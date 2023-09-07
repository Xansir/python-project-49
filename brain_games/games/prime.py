import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_task():
    question = random.randint(2, 100)
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            correct = 'no'
            break
        else:
            correct = 'yes'
    return question, correct
