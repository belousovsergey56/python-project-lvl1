"""Brain prime. Game.

The player must answer correctly three times a prime number or not.
"""
from random import SystemRandom


def brain_prime_rules() -> str:
    """Game rules.

    Function returns the rules of the game.

    Returns:
        str
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_prime_question() -> str:
    """Brain_prime_question.

    Function returns random number

    Returns:
        str
    """
    max_number = 3572
    number_to_returns = SystemRandom().randint(2, max_number)
    return str(number_to_returns)


def brain_prime_game_answer(quest) -> str:
    """Brain_game_answer.

    Function returns correct answer number is prime or not prime.
    yes or not

    Args:
        quest: str

    Returns:
        str
    """
    quest = int(quest)
    zero_counter = 0
    for numbers in range(1, quest + 1):
        if quest % numbers == 0:
            zero_counter += 1
    return 'yes' if zero_counter == 2 else 'no'
