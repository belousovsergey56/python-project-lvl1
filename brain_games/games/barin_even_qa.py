"""Brain even.

The methods of the game. The player is asked whether the number is even or odd.
The player wins if the answer is correct three times.
"""

from random import SystemRandom


def brain_even_rules() -> str:
    """Brain_even_rules. Returns rules this game.

    Returns:
        string
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_question() -> int:
    """Brain_even_questions.

    Returns random numbers, in 1 to 100.

    Returns:
        int
    """
    return SystemRandom().randint(1, 100)


def brain_even_check_number(random_num) -> bool:
    """Return True if number is even.

    If random_num % 2 == 0, number is even.

    Args:
        random_num: int

    Returns:
        bool
    """
    return random_num % 2 == 0
