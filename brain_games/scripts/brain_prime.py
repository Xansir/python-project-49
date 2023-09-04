import random
import prompt
from brain_games.scripts import brain_games1
import brain_games.cli

brain_games1.main()
win_count = 0
print('Answer "yes" if given number is prime. Otherwise answer "no".')
while win_count < 3:
    num = random.randint(2, 100)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            correct_answer = 'no'
            break
        if num % i != 0:
            correct_answer = 'yes'
    answer = prompt.string('Question: ' + str(num) + '\nYour answer:')
    if answer == str(correct_answer):
        print('Correct!')
        win_count += 1
    else:
        print("'" + str(answer) + "' is a wrong answer, correct answer was '" + str(correct_answer) + "'")
        brain_games.cli.user_lose()
        win_count = 0
        break
if win_count == 3:
    brain_games.cli.user_win()


def main():
    return None
