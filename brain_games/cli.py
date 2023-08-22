import prompt


def user_welcome():
    name = prompt.string('May I have your name? ')
    return print("Hello, " + name)

