"""
Modelling a python package

Name, Author, Version, Description
"""

from cmd import Cmd

from utils import Formatting
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

    def do_use(self, input):
        if input == '1':
            self.gen = TupleGen("Python Package", ['Name', 'Author', 'Version', 'Description'])
        elif input == '2':
            self.gen = TupleGen("Fruit", ['Name', 'Colour', 'Flavour'])
        elif input == '3':
            self.gen = TupleGen("Code Editor", ['Name', 'Developer', 'Primary Language', 'Price'])
        else:
            print("Please select one of the following by using 'use 1' to use example 1.")
            print("1    [ Python Package ] -- (Name, Author, Version, Description)")
            print("2    [      Fruit     ] -- (Name, Colour, Flavour)")
            print("3    [  Code Editor   ] -- (Name, Developer, Primary Language, Price)")

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
                    print(Formatting.error("Must have at least %d fields" % MIN_FIELDS))
                    continue
                else:
                    break

            field = field.upper()
            # prevent duplicate field names
            if field in fields:
                print(Formatting.error("A field with name %r already exists" % field))
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
        self.__print_tuple_list(self.tuple_list)

    def do_search(self, input):
        # TODO: find a tuple by search string
        if not self.__has_model():
            return

        if not self.__has_tuples():
            return

        if input == "":
            print(Formatting.error(
                "No search term provided.\nUse as 'search bob' where bob is the search term (case insensitive)."))
            return

        found = list(filter(lambda search_tuple: TupleGen.tuple_matches_query(search_tuple, input), self.tuple_list))

        no_found = len(found)
        if no_found == 0:
            print(Formatting.error("No tuples were found with that search string :("))
        else:
            print(Formatting.format("Found %d tuple%s..." % (no_found, "s" if no_found > 1 else ""), Formatting.GREEN))
            self.__print_tuple_list(found)

    def __has_model(self) -> bool:
        if self.gen is None:
            print(Formatting.error("No model set. Create one using the 'new' command."))
            return False
        return True

    def __has_tuples(self) -> bool:
        if len(self.tuple_list) == 0:
            print(Formatting.error("No tuples stored. Please add one using the 'add' command."))
            return False
        return True

    def __print_tuple_list(self, tuples):
        print(Formatting.title("--------[ Printing Tuples ]--------"))
        for t in tuples:
            self.gen.print_tuple(t)
        print(Formatting.title("-----------------------------------"))


if __name__ == '__main__':
    CmdPrompt().cmdloop()
