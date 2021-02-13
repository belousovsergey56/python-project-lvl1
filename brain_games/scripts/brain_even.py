#!/usr/bin/env python
"""Parity check. The Game."""
from brain_games.games.barin_even_qa import (
    brain_even_check_number,
    brain_even_question,
    brain_even_rules,
)
from brain_games.kernel import run


def main():
    """Game launch."""
    rules = brain_even_rules
    question = brain_even_question
    answer = brain_even_check_number
    run(rules, question, answer)


if __name__ == '__main__':
    main()
