import random

DESCRIPTION = "What number is missing in the progression?"


def game_task():
    num_ls = [random.randint(0, 10)]
    up_count = random.randint(1, 20)
    for i in range(10):
        num_ls.append(num_ls[i] + up_count)
    correct = random.choice(num_ls)
    for i in range(len(num_ls)):
        if num_ls[i] == correct:
            num_ls[i] = '..'
    question = " ".join(str(x) for x in num_ls)
    return question, correct
