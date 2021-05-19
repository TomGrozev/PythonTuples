from utils import Formatting, prompt, print_model


class Generator(object):
    out_type = dict

    def __init__(self, object, fields) -> None:
        super().__init__()

        self.object = object
        self.fields = fields

    def new(self) -> out_type:
        print(Formatting.title("---------[ New %s ]---------" % self.object))

        field_responses = {}
        for field in self.fields:
            field_responses[field] = prompt(field)

        new_item = self.__generator__(**field_responses)
        print("")
        print_model(self.__singular__(new_item))

        return new_item

    def __singular__(self, item):
        return item.__str__()

    @staticmethod
    def __generator__(**kwargs) -> out_type:
        return kwargs
