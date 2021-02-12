"""Calculate the result of the expression. The game."""
from brain_games.kernel import (
    check_end_game,
    welcome_the_game_user,
    ask_player_take_answer,
)
from brain_games.games.brain_calc_qa import (
    brain_calc_check_expression,
    brain_calc_rules,
    brain_calc_question,
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
    player_name = welcome_the_game_user(brain_calc_rules())
    for trying in range(3):
        question = brain_calc_question()
        answer = ask_player_take_answer(question)
        correct_answer = brain_calc_check_expression(question)
        if check_end_game(trying, answer, correct_answer, player_name):
            continue
        break


if __name__ == '__main__':
    main()
