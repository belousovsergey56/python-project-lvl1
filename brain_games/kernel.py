#!/usr/bin/env python
"""
Game Engine.

This module contains functions - interfaces for using and implementing games.
"""
from prompt import string

GREETING = 'Welcome to the Brain Games!'
IS_WRONG = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
TRY_AGAIN = "Let's try again, {0}!"
VICTORY = 'Congratulations, {0}!'
CORRECT = 'Correct!'


def welcome_the_game_user(rules: str) -> str:
    """Welcome.

     Function greeting user and ask users name.
     And returns this value.
     Function display the game rules.

    Args:
        rules: str

    Returns:
            str, user name
    """
    print(GREETING)
    name = string('May I have your name? ').title()
    print('Hello, {0}!'.format(name))
    print(rules)
    return name


def ask_player_take_answer(question):
    """Player answer.

    Function takes the game question.
    Outputs it to the player.
    Accepts his answer.
    Returns a string with the answer.

    Args:
        question: int, str

    Returns:
        answer: The string
    """
    print('Question:', question)
    return input('Your answer: ')


def check_end_game(trying, user_resp, game_resp, user_name):
    """End Game Check.

    The function spins the player's answer and the game's answer.
    And displays the message 'Correct answer', 'Win' or 'Defeat'.

    Args:
        trying: int
        user_resp: string, user response
        game_resp: string, game response
        user_name: string, user/player name

    Returns:
        True or False
    """
    if user_resp == game_resp:
        print(CORRECT)
        print(VICTORY.format(user_name)) if trying == 2 else None
        return True
    else:
        print(IS_WRONG.format(user_resp, game_resp))
        print(TRY_AGAIN.format(user_name))
        return False


def run(rules, game_question, game_answer):
    """Run game.

    1. Welcome the Brain Game
    2. Game, ask user name
    3. Hello, user name
    4. Display rules
    5. Question for user
    6. User must give three correct response
    7. Game over

    Args:
         rules: str, game rules
         game_question: str
         game_answer: str

    """
    player_name = welcome_the_game_user(rules())
    for trying in range(3):
        question = game_question()
        answer = ask_player_take_answer(question)
        correct_answer = game_answer(question)
        if check_end_game(trying, answer, correct_answer, player_name):
            continue
        break
