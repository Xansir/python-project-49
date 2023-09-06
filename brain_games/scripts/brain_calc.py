import random
import prompt
from brain_games.scripts import brain_games1
import brain_games.cli

brain_games1.main()
win_count = 0
while win_count < 3:
    print('What is the result of the expression?')
    num1 = random.randint(0, 30)
    num2 = random.randint(0, 30)
    act = random.choice(['+', '-', '*'])
    if act == '-':
        correct_answer = (num1 - num2)
    if act == '+':
        correct_answer = (num1 + num2)
    if act == '*':
        correct_answer = (num1 * num2)
    print(f'Question: {num1} {act} {num2}')
    answer = prompt.string('Your answer:')
    if answer == str(correct_answer):
        print('Correct!')
        win_count += 1
    else:
        print(str(answer) + ' is a wrong answer, correct answer was ' + str(correct_answer))
        brain_games.cli.user_lose()
        win_count = 0
        break
if win_count == 3:
    brain_games.cli.user_win()


def main():
    return None


if __name__ == '__main__':
    main()

