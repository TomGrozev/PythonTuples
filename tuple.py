from prompt import prompt


class TupleGen:

    def __init__(self, object, fields) -> None:
        super().__init__()

        self.object = object
        self.fields = fields

    def new(self) -> tuple:
        print("---------[ New %s ]---------" % self.object)

        field_responses = {}
        for field in self.fields:
            field_responses[field] = prompt(field)

        new_tuple = self.__class__.__create_tuple(**field_responses)

        print(self.object + new_tuple.__str__())
        return new_tuple

    @staticmethod
    def __create_tuple(**kwargs) -> tuple:
        ordered_vals = kwargs.values()
        return tuple(ordered_vals)
