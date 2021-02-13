"""Brain progression.

The game is up to three wins.
The player is given a random arithmetic progression
The random number in the progression is stitched and must be guessed.
The length of the progression is from 5 to 10 numbers.

"""
from random import SystemRandom

min_length = 10  # minimal progression length
max_length = 20  # maximal progression length


def brain_progression_rules() -> str:
    """Game rules.

    Function returns the rules of the game.

    Returns:
        str
    """
    return 'What number is missing in the progression?'


def random_progression() -> list:
    """Random progression.

    The function has the variables
    start, progression start
    stop, progression length
    step, step of progression

    Returns:
         list
    """
    start = SystemRandom().randint(1, 100)
    stop = SystemRandom().randint(min_length, max_length) + start
    step = SystemRandom().randint(2, 4)
    progression_list = []

    while len(progression_list) < 5 or len(progression_list) >= 10:
        for numbers in range(start, stop, step):
            progression_list.append(str(numbers))
    return progression_list


def brain_progression_question() -> str:
    """Brain question.

    Function returns random arithmetic progression
    Random number in the progression is stitched and must be guessed
    Length of the progression is from 5 to 10 numbers

    Returns: str
    """
    pass
