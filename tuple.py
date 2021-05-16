from utils import *

class TupleGen:

    def __init__(self, object, fields) -> None:
        super().__init__()

        self.object = object
        self.fields = fields

    def new(self) -> tuple:
        print("---------[ New %s ]---------" % self.object)

        field_responses = {}
        for field in self.fields:
            field_responses[field] = self.__class__.__prompt(field)

        new_tuple = self.__class__.__create_tuple(**field_responses)

        print(self.object + new_tuple.__str__())
        return new_tuple

    @staticmethod
    def __prompt(message) -> str:
        # trim whitespace from ends
        message = message.strip()

        # Add ':' if missing
        if message[-1] != ':':
            message += ':'

        message += ' '

        return input(format(message, formatting.BOLD))

    @staticmethod
    def __create_tuple(**kwargs) -> tuple:
        ordered_vals = kwargs.values()
        return tuple(ordered_vals)
