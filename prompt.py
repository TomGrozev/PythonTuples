from utils import Formatting


def prompt(message) -> str:
    # trim whitespace from ends
    message = message.strip()

    # Add ':' if missing
    if message[-1] != ':':
        message += ':'

    message += ' '

    return input(Formatting.format(message, Formatting.BOLD))
