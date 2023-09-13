import random
import operator

DESCRIPTION = "What is the result of the expression?"


def play_game():
    num1 = random.randint(0, 30)
    num2 = random.randint(0, 30)
    act = random.choice(['+', '-', '*'])
    if act == '-':
        correct = operator.add(num1, num2)
    if act == '+':
        correct = operator.sub(num1, num2)
    if act == '*':
        correct = operator.mul(num1, num2)
    question = f"{num1} {act} {num2}"
    return question, correct
