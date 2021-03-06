from gen import Generator


class TupleGen(Generator):
    out_tupe = tuple

    def __singular__(self, item):
        return self.object + item.__str__()

    def __generator__(self, **kwargs) -> tuple:
        ordered_vals = kwargs.values()
        return tuple(ordered_vals)
