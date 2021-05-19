
class Model(object):

    def __init__(self, **kwargs) -> None:
        super().__init__()

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        templ = ", ".join(["%s=%r" % (k, v) for k, v in self.__dict__.items()])
        return "%s(%s)" % (self.__class__.__name__, templ)

