"""Brain progression.

Script run game.
"""
from brain_games.games.brain_progression_qa import (
    brain_game_answer,
    brain_progression_question,
    brain_progression_rules,
)
from brain_games.kernel import run


def main():
    """Game launch."""
    rules = brain_progression_rules
    question = brain_progression_question
    answer = brain_game_answer
    run(rules, question, answer)


if __name__ == '__main__':
    main()
