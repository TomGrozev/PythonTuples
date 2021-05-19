from storage import Store


class ClassStore(Store):
    type = 'Class'

    def __search_comparator__(self, item, query):
        for v in item.__dict__.values():
            if v.__str__().lower().startswith(query):
                return True
        return False

    def __singular__(self, item):
        return item.__str__()

    def __update_search__(self, item):
        item.searched += 1
        return item
