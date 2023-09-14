#!/usr/bin/env python3
import prompt


def user_welcome():
    name = prompt.string('May I have your name? ')
    return print('Hello, ' + name)
