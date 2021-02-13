"""Greatest common divisor of two numbers.

The game sets two numbers, the player must find the greatest common divisor.
"""
from math import gcd
from random import SystemRandom


def brain_game_gcd_rules() -> str:
    """Game rules.

    Function returns the rules of the game

    Returns:
        str
    """
    return 'Find the greatest common divisor of given numbers.'


def brain_game_gcd_question():
    """Brain_gcd_question.

    Function generate two random numbers in 1 to 100

    Returns:
        two random numbers: tuple

    """
    first_number = SystemRandom().randint(1, 100)
    second_number = SystemRandom().randint(1, 100)
    return first_number, second_number


def brain_game_gcd_correct_answer(number_one, number_two):
    """Game answer.

    Args:
        number_one: int
        number_two: int

    Returns:
        str
    """
    return str(gcd(number_one, number_two))
