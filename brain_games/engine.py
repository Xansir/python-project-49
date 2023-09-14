import prompt

WINSTRIKE = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n')
    print('Hello, ' + name)
    print(game.DESCRIPTION)
    win_count = 0
    while win_count < WINSTRIKE:
        question, correct = game.play_game()
        if answer_comparsion(question, correct):
            win_count += 1
        else:
            return print(f"Let's try again, {name}!")
    if win_count == WINSTRIKE:
        print(f"Congratulations, {name}!")


def answer_comparsion(question, correct):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == str(correct):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is a wrong answer. correct answer was '{correct}'")
        return False
