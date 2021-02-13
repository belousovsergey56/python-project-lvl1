"""Brain_gcd. Game.

The game script in function.
"""
from brain_games.games.brain_gcd_qa import (
    brain_game_gcd_correct_answer,
    brain_game_gcd_question,
    brain_game_gcd_rules,
)
from brain_games.kernel import (
    ask_player_take_answer,
    check_end_game,
    welcome_the_game_user,
)


def main():
    """Logic game.

    Implementation:
    1. Welcome the Brain Game
    2. Game, ask user name
    3. Hello, user name
    4. Display rules
    5. Question for user
    6. User must give three correct response
    7. Game over

    """
    player_name = welcome_the_game_user(brain_game_gcd_rules())
    for trying in range(3):
        question = brain_game_gcd_question()
        answer = ask_player_take_answer(question)
        correct_answer = brain_game_gcd_correct_answer(question)
        if check_end_game(trying, answer, correct_answer, player_name):
            continue
        break


if __name__ == '__main__':
    main()
