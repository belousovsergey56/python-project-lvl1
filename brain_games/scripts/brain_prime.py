"""Brain prime. Game."""
from brain_games.games.brain_prime_qa import (
    brain_prime_game_answer,
    brain_prime_question,
    brain_prime_rules,
)
from brain_games.kernel import run


def main():
    """Script to run game."""
    rules = brain_prime_rules
    question = brain_prime_question
    answer = brain_prime_game_answer
    run(rules, question, answer)


if __name__ == '__main__':
    main()
