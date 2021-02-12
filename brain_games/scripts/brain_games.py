#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    """Display Greeting."""
    print("Welcome to the Brain Games!")
    print("Hello, {}!".format(welcome_user()))


if __name__ == '__main__':
    main()
