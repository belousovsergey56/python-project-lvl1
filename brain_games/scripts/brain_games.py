#!/usr/bin/env python
"""Simple module, with import and function Greeting user."""
from sys import stdout

from brain_games.cli import welcome_user

WELCOME = 'Welcome to the Brain Games!\n'
GREETING = 'Hello, {0}!\n'


def main():
    """Display Greeting."""
    stdout.writelines(WELCOME)
    stdout.writelines(GREETING.format(welcome_user()))


if __name__ == '__main__':
    main()
