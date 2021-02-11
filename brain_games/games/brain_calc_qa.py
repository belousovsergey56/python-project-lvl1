"""Brain-calc.

The game gives the problem of adding, subtracting or multiplying two numbers.
The player must give the correct answer three times.
"""
import operator
from random import SystemRandom

LIMIT_NUMBER = 50
RANDOM_OPERATORS = ('+', '*', '-')
OPERATORS = (operator.add, operator.mul, operator.sub)


def brain_calc_rules() -> str:
    """Brain_calc_rules.

    This function returns rules this game.

    Returns:
        string

    """
    return 'What is the result of the expression?'


def brain_calc_question() -> str:
    """Brain_calc_question.

    The function takes random numbers and returns an expression
    with a random operator, '+', '-', '*', as a string.
    Template: x1 + x2; x1 - x2; x1 * x2

    Returns:
        str

    """
    first_number = SystemRandom().randint(LIMIT_NUMBER, 100)
    second_number = SystemRandom().randint(1, LIMIT_NUMBER)
    sign = SystemRandom().choice(RANDOM_OPERATORS)
    question = '{0} {1} {2}'
    return question.format(first_number, sign, second_number)


def brain_calc_check_expression(string_q: str) -> int:
    """Check expression.

    The function accepts a string. Expression.
    Extracts numbers and a sign to a list.
    The function then calculates the expression and returns the result as int.

    Args:
        string_q: str, questions

    Returns:
        integer

    """
    split_expression = string_q.split()
    first_number = int(split_expression[0])
    second_number = int(split_expression[2])
    sign = split_expression[1]
    if sign == '+':
        return OPERATORS[0](first_number, second_number)
    elif sign == '*':
        return OPERATORS[1](first_number, second_number)
    elif sign == '-':
        return OPERATORS[2](first_number, second_number)
