import prompt
import brain_games.cli
from brain_games.scripts import brain_games_module

WINSTRIKE = 3


def start_game(game):
    brain_games_module.main()
    print(game.DESCRIPTION)
    win_count = 0
    while win_count < WINSTRIKE:
        question, correct = game.play_game()
        if answer_comparsion(question, correct):
            win_count += 1
        else:
            return print(f"Let's try again, {brain_games.cli.name}!")
    if win_count == WINSTRIKE:
        print(f"Congratulations, {brain_games.cli.name}!")


def answer_comparsion(question, correct):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == str(correct):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is a wrong answer. correct answer was '{correct}'")
        return False
