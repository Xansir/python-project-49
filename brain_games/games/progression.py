import random

DESCRIPTION = "What number is missing in the progression?"


def play_game():
    progression = []
    up_count = random.randint(1, 10)
    for i in range(random.randint(0, 10), 100, up_count):
        progression.append(i)
    index = random.choice(range(len(progression)))
    correct = progression[index]
    progression[index] = '..'
    question = " ".join(str(x) for x in progression)
    return question, correct
