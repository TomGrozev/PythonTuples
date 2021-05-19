from gen import Generator
from model import Model


class ClassGen(Generator):
    out_tupe = Model.__class__

    def __generator__(self, **kwargs) -> Model:
        cls = type(self.object, (Model,), {})
        return cls(**kwargs)
