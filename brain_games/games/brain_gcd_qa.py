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
        two random numbers: str

    """
    first_number = SystemRandom().randint(1, 100)
    second_number = SystemRandom().randint(1, 100)
    question = '{0} {1}'
    return question.format(first_number, second_number)


def brain_game_gcd_correct_answer(question):
    """Game answer.

    Args:
        question: str

    Returns:
        str
    """
    numbers = question.split(' ')
    number_one = int(numbers[0])
    number_two = int(numbers[1])
    return str(gcd(number_one, number_two))
