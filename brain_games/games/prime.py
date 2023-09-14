import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    question = random.randint(2, 100)
    if is_prime(question):
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct


def is_prime(question):
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return False
    return True
