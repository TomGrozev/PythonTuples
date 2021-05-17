from utils import *


def prompt(message) -> str:
    # trim whitespace from ends
    message = message.strip()

    # Add ':' if missing
    if message[-1] != ':':
        message += ':'

    message += ' '

    return input(format_cmd(message, formatting.BOLD))
