class Formatting:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    @staticmethod
    def format(message: str, formatting: str or list) -> str:
        if isinstance(formatting, list):
            formatting = ''.join(formatting)

        return formatting + message + '\033[0m'

    @staticmethod
    def error(message: str) -> str:
        return Formatting.format(message, [Formatting.RED, Formatting.BOLD])

    @staticmethod
    def title(message: str) -> str:
        return Formatting.format(message, [Formatting.YELLOW, Formatting.BOLD])


def capitalise_str(string):
    return " ".join([word.capitalize() for word in string.split(" ")])

def prompt(message) -> str:
    # trim whitespace from ends
    message = message.strip()

    # Add ':' if missing
    if message[-1] != ':':
        message += ':'

    message += ' '

    return input(Formatting.format(message, Formatting.BOLD))
