#!/usr/bin/env python
"""Simple module, with import and function Greeting user."""
from brain_games.cli import welcome_user

WELCOME = 'Welcome to the Brain Games!'
GREETING = 'Hello, {0}!'


def main():
    """Display Greeting."""
    print(WELCOME)
    print(GREETING.format(welcome_user()))


if __name__ == '__main__':
    main()
