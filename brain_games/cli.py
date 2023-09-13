name = None


def user_welcome():
    print('May I have your name?')
    global name
    name = input()
    return print('Hello, ' + name)
