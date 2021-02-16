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


def brain_progression_question() -> str:
    """Brain_progression_question.

    Function take a list, replace random number and return string numbers

    Returns:
        str

    """
    random_progression()
    secret_num = SystemRandom().choice(progression_list)
    question = ''

    for key, numbers in enumerate(progression_list):
        if secret_num == numbers:
            question += (
                dots if key == len(progression_list) - 1 else dots + space
            )
        else:
            question += (
                str(numbers) if key == len(progression_list) - 1
                else str(numbers) + space
            )
    return question


def brain_game_answer(question: str) -> str:
    """Game answer.

    Args:
        question: str

    Returns:
        str
    """
    question_to_list = question.split(' ')
    dots_index = question_to_list.index('..')
    return str(progression_list.pop(dots_index))
