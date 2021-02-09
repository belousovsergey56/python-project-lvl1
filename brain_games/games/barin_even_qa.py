"""Brain even.

The methods of the game. The player is asked whether the number is even or odd.
The player wins if the answer is correct three times.
"""
from random import randint


def brain_even_rules() -> str:
    """Brain_even_rules. Returns rules this game.

    Returns:
        string
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_question() -> int:
    """Brain_even_questions.

    Returns random numbers, period 1 to 100.

    Returns:
        int
    """
    return randint(1, 100)