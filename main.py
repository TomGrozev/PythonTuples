"""
Modelling a python package

Name, Author, Version, Description
"""

from cmd import Cmd

from prompt import prompt
from tuple import TupleGen

MIN_FIELDS = 3
MAX_FIELDS = 10


class CmdPrompt(Cmd):
    prompt = 'Modeler> '
    intro = 'Welcome to the MODELER! Use ? command to list commands'

    gen = None
    tuple_list = []

    def do_exit(self, input):
        print("Exiting...")
        return True

    def do_new(self, object):
        '''Creates a new model'''
        if object == "":
            # prompt for object
            object = prompt("Type of object")

        object = object.upper()

        # prompt for field list
        print("Please enter the fields, this model will have (min %d, max %d)." % (MIN_FIELDS, MAX_FIELDS))
        print("To finish entering fields enter 'q'.")
        fields = []
        i = 1
        while i <= MAX_FIELDS:
            field = prompt("Field %d name" % i)

            if field == 'q':
                if i <= MIN_FIELDS:
                    print("Must have at least %d fields" % MIN_FIELDS)
                    continue
                else:
                    break

            field = field.upper()
            # prevent duplicate field names
            if field in fields:
                print("A field with name %r already exists" % field)
                continue

            fields.append(field)
            i += 1

        print("%s fields: %s" % (object, ', '.join(fields)))

        self.gen = TupleGen(object, fields)


    def do_add(self, input):
        '''Adds a new tuple to the store'''
        if not self.__has_model():
            return

        new_tuple = self.gen.new()
        self.tuple_list.append(new_tuple)

    def do_list(self, input):
        # TODO: formatting
        print(self.tuple_list)

    def do_search(self, input):
        # TODO: find a tuple by search string
        if not self.__has_model():
            return

        if not self.__has_tuples():
            return

        if input == "":
            print("No search term provided.\nUse as 'search bob' where bob is the search term (case insensitive).")
            return

        found = list(filter(lambda search_tuple: TupleGen.tuple_matches_query(search_tuple, input), self.tuple_list))
        print(found)

    def __has_model(self) -> bool:
        if self.gen is None:
            print("No model set. Create one using the 'new' command.")
            return False
        return True

    def __has_tuples(self) -> bool:
        if len(self.tuple_list) == 0:
            print("No tuples stored. Please add one using the 'add' command.")
            return False
        return True




if __name__ == '__main__':
    CmdPrompt().cmdloop()
