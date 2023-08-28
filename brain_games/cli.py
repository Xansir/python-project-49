import prompt
name = None


def user_welcome():
    print('May I have your name?')
    global name
    name = input()
    return print('Hello, ' + name)


def user_win():
    print('Congratulations, ' + name + '!')


def user_lose():
    print("Let's try again " + name + '!')

