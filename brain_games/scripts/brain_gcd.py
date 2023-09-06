import random
import prompt
import math
from brain_games.scripts import brain_games1
import brain_games.cli

brain_games1.main()
win_count = 0
while win_count < 3:
    print('Find the greatest common divisor of given numbers.')
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = math.gcd(num1, num2)
    answer = prompt.string(f'Question: {num1} {num2}\nYour answer:')
    if answer == str(correct):
        print('Correct!')
        win_count += 1
    else:
        print(f"'{answer}' is a wrong answer, correct answer was '{correct}'")
        brain_games.cli.user_lose()
        win_count = 0
        break
if win_count == 3:
    brain_games.cli.user_win()


def main():
    return None


if __name__ == '__main__':
    main()
