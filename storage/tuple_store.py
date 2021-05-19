from storage import Store


class TupleStore(Store):
    type = 'Tuple'

    def __search_comparator__(self, item, query):
        for attr in item:
            if attr.lower().startswith(query):
                return True
        return False

    def __singular__(self, item):
        return self.object + item.__str__()
