import prompt
import brain_games.cli
from brain_games.scripts import brain_games1


def game_logic(game):
    brain_games1.main()
    print(game.DESCRIPTION)
    win_count = 0
    while win_count < 3:
        question, correct = game.game_task()
        if game_try(question, correct):
            win_count += 1
        else:
            return brain_games.cli.user_lose()
    if win_count == 3:
        brain_games.cli.user_win()


def game_try(question, correct):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == str(correct):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is a wrong answer. correct answer was '{correct}'")
        return False
