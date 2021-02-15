"""Brain progression.

The game is up to three wins.
The player is given a random arithmetic progression
The random number in the progression is stitched and must be guessed.
The length of the progression is from 5 to 10 numbers.

"""
from random import SystemRandom

min_limit = 10  # minimal progression length
max_limit = 31  # maximal progression length
diff_limits = 20
progression_list = []
dots = '..'
space = ' '


def brain_progression_rules() -> str:
    """Game rules.

    Function returns the rules of the game.

    Returns:
        str
    """
    return 'What number is missing in the progression?'


def random_progression():
    """Random progression.

    The function has the variables
    start, progression start
    stop, progression length
    step, step of progression

    """
    progression_list.clear()
    start = SystemRandom().randint(0, 100)
    stop = SystemRandom().randint(min_limit, max_limit) + start
    step = 0
    if stop - start < diff_limits:
        step += 2
    else:
        step += SystemRandom().randint(3, 5)
    for numbers in range(start, stop, step):
        progression_list.append(numbers)


def brain_progression_question(_list: list) -> str:
    """Brain_progression_question.

    Function take a list, replace random number and return string numbers

    Args:
        _list: progression list

    Returns:
        str

    """
    secret_num = SystemRandom().choice(_list)
    question = ''

    for key, numbers in enumerate(_list):
        if secret_num == numbers:
            question += dots if key == len(_list) - 1 else dots + space
        else:
            question += (
                str(numbers) if key == len(_list) - 1
                else str(numbers) + space
            )
    return question, secret_num
