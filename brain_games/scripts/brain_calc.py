"""Calculate the result of the expression. The game."""
from brain_games.games.brain_calc_qa import (
    brain_calc_check_expression,
    brain_calc_question,
    brain_calc_rules,
)
from brain_games.kernel import run


def main():
    """Game launch."""
    rules = brain_calc_rules
    question = brain_calc_question
    answer = brain_calc_check_expression
    run(rules, question, answer)


if __name__ == '__main__':
    main()
