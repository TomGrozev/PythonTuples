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

    def __update_search__(self, item):
        # Since tuples are not separate instances like classes, holding the searched number info is not feasible.
        # This is possible but would require modifying the storage class to not be a list and rather be an object
        # containing a list.
        return item
