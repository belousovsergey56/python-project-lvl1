"""Brain_gcd. Game.

The game script in function.
"""
from brain_games.games.brain_gcd_qa import (
    brain_game_gcd_correct_answer,
    brain_game_gcd_question,
    brain_game_gcd_rules,
)
from brain_games.kernel import run


def main():
    """Game launch."""
    rules = brain_game_gcd_rules
    question = brain_game_gcd_question
    answer = brain_game_gcd_correct_answer
    run(rules, question, answer)


if __name__ == '__main__':
    main()
