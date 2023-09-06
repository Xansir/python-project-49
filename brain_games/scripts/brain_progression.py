import prompt
import random
from brain_games.scripts import brain_games1
import brain_games.cli

brain_games1.main()
win_count = 0
print('What number is missing in the progression?')
while win_count < 3:
    num_ls = [random.randint(0, 10)]
    up_count = random.randint(1, 20)
    for i in range(10):
        num_ls.append(num_ls[i] + up_count)
    correct = random.choice(num_ls)
    for i in range(len(num_ls)):
        if num_ls[i] == correct:
            num_ls[i] = '..'
    progression = " ".join(str(x) for x in num_ls)
    answer = prompt.string(f'Question: {progression}\nYour answer: ')
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
