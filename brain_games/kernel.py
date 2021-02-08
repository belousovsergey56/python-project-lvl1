#!/usr/bin/env python
"""
Game Engine.

This module contains functions - interfaces for using and implementing games.
"""
GRETEENG = 'Welcome to the Brain Games!'
IS_WRONG = "'{1}' is wrong answer ;(. Correct answer was '{2}'."
TRY_AGAIN = "Let's try again, {1}!"


def welcome_to_the_game():
    """Do this print greteeng."""
    print(GRETEENG)


def game_rules(rules: str):
    """Do this function takes a string of game rules.

    Args:
        rules: The string
    """
    print(rules)


def player_answer(question: str):
    """Player answer.

    The function takes the game question.
    Outputs it to the player.
    Accepts his answer.
    Returns a string with the answer.

    Args:
        question: The string

    Returns:
        answer: The string
    """
    print('Question:', question)
    return input('Your answer: ')


def display_wrong_answer(player_response, correct_answer, player_name):
    """Display in console message correct and wrong answer.

    Args:
        player_response: The string
        correct_answer: The string
        player_name: The string
    """
    print(IS_WRONG.format(player_response, correct_answer))
    print(TRY_AGAIN.format(player_name))
