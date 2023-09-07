import math
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def game_task():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, correct
