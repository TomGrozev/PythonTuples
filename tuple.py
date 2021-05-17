from prompt import prompt
from utils import Formatting


class TupleGen:

    def __init__(self, object, fields) -> None:
        super().__init__()

        self.object = object
        self.fields = fields

    def new(self) -> tuple:
        print(Formatting.title("---------[ New %s ]---------" % self.object))

        field_responses = {}
        for field in self.fields:
            field_responses[field] = prompt(field)

        new_tuple = self.__class__.__create_tuple(**field_responses)
        print("")
        self.print_tuple(new_tuple)

        return new_tuple

    def print_tuple(self, in_tuple):
        print(Formatting.format("~~>  ", [Formatting.BOLD, Formatting.CYAN]) + Formatting.format(
            self.object + in_tuple.__str__(), Formatting.CYAN))

    @staticmethod
    def tuple_matches_query(search_tuple, query) -> bool:
        query = query.lower()
        for item in search_tuple:
            if item.lower().startswith(query):
                return True
        return False

    @staticmethod
    def __create_tuple(**kwargs) -> tuple:
        ordered_vals = kwargs.values()
        return tuple(ordered_vals)
