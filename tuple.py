from prompt import prompt
from utils import Formatting


def print_tuple(object, in_tuple):
    print(Formatting.format("~~>  ", [Formatting.BOLD, Formatting.CYAN]) + Formatting.format(
        object + in_tuple.__str__(), Formatting.CYAN))


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
        print_tuple(self.object, new_tuple)

        return new_tuple

    @staticmethod
    def __create_tuple(**kwargs) -> tuple:
        ordered_vals = kwargs.values()
        return tuple(ordered_vals)


class TupleStore(list):
    object = "Tuple"

    def __init__(self, *args, **kwargs) -> None:
        super(TupleStore, self).__init__(*args)
        if 'object' in kwargs:
            self.object = kwargs.get('object')

    def find_tuples(self, query):
        return TupleStore(filter(lambda search_tuple: self.__tuple_matches_query(search_tuple, query), self),
                          object=self.object)

    def print(self):
        if len(self) == 0:
            print(Formatting.error("No tuples stored. Please add one using the 'add' command."))
            return

        print(Formatting.title("--------[ Printing Tuples ]--------"))
        for t in self:
            print_tuple(self.object, t)
        print(Formatting.title("-----------------------------------"))

    @staticmethod
    def __tuple_matches_query(search_tuple, query) -> bool:
        query = query.lower()
        for item in search_tuple:
            if item.lower().startswith(query):
                return True
        return False
