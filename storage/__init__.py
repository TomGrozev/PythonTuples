from utils import Formatting, print_model


class Store(list):
    type = 'List'

    def __init__(self, object, *args) -> None:
        super(Store, self).__init__(*args)
        self.object = object

    def search(self, query):
        query = query.lower()
        return self.__class__(self.object, filter(lambda item: self.__search_comparator__(item, query), self))

    def print(self):
        if len(self) == 0:
            print(Formatting.error("Storage Empty. Add an item using the 'add' command."))
            return

        print(Formatting.title("--------[ Printing %s ]--------" % self.type))
        for t in self:
            print_model(self.__singular__(t))
        print(Formatting.title("-----------------------------------"))

    def __search_comparator__(self, item, query):
        return item == query

    def __singular__(self, item):
        return item.__str__()
