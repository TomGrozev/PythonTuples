from storage import Store


class TupleStore(Store):
    type = 'Tuple'

    def __search_comparator__(self, item, query):
        return self.__tuple_matches_query(item, query)

    def __singular__(self, item):
        return self.object + item.__str__()

    @staticmethod
    def __tuple_matches_query(search_tuple, query) -> bool:
        query = query.lower()
        for item in search_tuple:
            if item.lower().startswith(query):
                return True
        return False
