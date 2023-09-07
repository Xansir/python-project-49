import random

DESCRIPTION = "What is the result of the expression?"


def game_task():
    num1 = random.randint(0, 30)
    num2 = random.randint(0, 30)
    act = random.choice(['+', '-', '*'])
    if act == '-':
        correct = (num1 - num2)
    if act == '+':
        correct = (num1 + num2)
    if act == '*':
        correct = (num1 * num2)
    question = f"{num1} {act} {num2}"
    return question, correct
