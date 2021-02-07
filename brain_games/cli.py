"""Module for function 'welcome user'."""
import prompt


def welcome_user() -> str:
    """Funtion ask users name.

    Returns:
            str, user name
    """
    return prompt.string('May I have your name? ')
