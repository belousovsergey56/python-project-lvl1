#!/usr/bin/env python
"""
Game Engine.

This module contains functions - interfaces for using and implementing games.
"""


def welcome_to_the_game():
    """Do this print greteeng."""
    greeteng = 'Welcome to the Brain Games!'
    print(greeteng)


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
