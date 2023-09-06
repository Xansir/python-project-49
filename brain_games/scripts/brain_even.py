import random
import prompt
from brain_games.scripts import brain_games1
import brain_games.cli

# Easy game choice is number even


brain_games1.main()
print('Answer "yes" if the number is even, otherwise answer "no".')
win_count = 0
while win_count < 3:
    number = random.randint(0, 40)
    print(f"Question: {number}")
    answer = prompt.string('Your answer: ')
    if number % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    if answer == correct:
        print('Correct!')
        win_count += 1
    else:
        print(f"'{answer}' is a wrong answer. correct answer was '{correct}'")
        brain_games.cli.user_lose()
        win_count = 0
        break
if win_count == 3:
    brain_games.cli.user_win()


def main():
    return None


if __name__ == '__main__':
    main()
