#!/usr/bin/env python
"""Parity check. The Game."""
from kernel import welcome_user, welcome_to_the_game, player_answer
from kernel import game_rules, check_end_game
from barin_even_qa import brain_even_rules, brain_even_question
from barin_even_qa import brain_even_check_number


def main():
    """Logic game.

    1. Welcome the Brain Game
    2. Game, ask user name
    3. Hello, user name
    4. Display rules
    5. Question for user
    6. User must give three correct response
    7. Game over

    """
    welcome_to_the_game()
    player_name = welcome_user()
    game_rules(brain_even_rules())
    for trying in range(3):
        question = brain_even_question()
        answer = player_answer(question)
        correct_answer = 'yes' if brain_even_check_number(question) else 'no'
        if check_end_game(trying, answer, correct_answer, player_name):
            continue
        break


if __name__ == '__main__':
    main()
