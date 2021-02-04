#!/usr/bin/env python
"""Parity check. The Game."""

import prompt
from random import randint

welcome = 'Welcome to the Brain Games!'
display_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
player = str
random_num = int
answer = str
YES = 'yes'
NO = 'no'


def show_rules():
    """displays the rules of the game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def welcome_game():
    """Print to display welcome."""
    print('Welcome to the Brain Games!')


def get_random_number() -> int:
    """Return random number"""
    return randint(1, 100)


def check_even_number(random_num) -> bool:
    """Return True if  number is even"""
    return random_num % 2 == 0


def check_end_game(answer, random_num, player) -> bool:
    """Check victory and finish game"""
    comment = "{} is wrong answer ;(. Correct answer was '{}'."
    even = check_even_number(random_num)
    if even and answer == YES or not even and answer == NO:
        print('Correct!')
        return True
    elif (even and answer == YES) or (not even and answer == YES) \
            or (answer != YES or answer != NO):
        print(comment.format(answer, YES if even else NO))

        print("Let's try again, {}!".format(player))
        return False



def main(): # noqa E303
    welcome_game()
    player = prompt.string('May I have your name? ').title()
    print('Hello, {}'.format(player))
    print(display_rules)
    for trying in range(3):
        random_num = get_random_number()
        print('Question:', random_num)
        answer = input('Your answer: ')
        if not check_end_game(answer, random_num, player):
            break
        else:
            continue
    print("Congratulations, {}!".format(player)) if trying == 2 else None


if __name__ == '__main__':
    main()
