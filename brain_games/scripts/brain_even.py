#!/usr/bin/env python
"""Parity check. The Game."""
from brain_games.kernel import (
    welcome_the_game_user,
    ask_player_take_answer,
    check_end_game,
)
from brain_games.games.barin_even_qa import (
    brain_even_rules,
    brain_even_question,
    brain_even_check_number,
)


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
    player_name = welcome_the_game_user(brain_even_rules())
    for trying in range(3):
        question = brain_even_question()
        answer = ask_player_take_answer(question)
        correct_answer = 'yes' if brain_even_check_number(question) else 'no'
        if check_end_game(trying, answer, correct_answer, player_name):
            continue
        break


if __name__ == '__main__':
    main()
