"""Module for function 'welcome user'."""
import prompt


def welcome_user() -> str:
    """Funtion ask users name.

    Returns:
            str, user name
    """
    return prompt.string('May I have your name? ')


def welcome_to_the_game():
    """Do this print greteeng."""
    greeteng = 'Welcome to the Brain Games!'
    print(greeteng)
