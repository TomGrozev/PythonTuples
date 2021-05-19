"""
Modelling a python package

Name, Author, Version, Description
"""

from cmd import Cmd

from utils import Formatting, capitalise_str, prompt
from tuple import TupleGen, TupleStore

NAME = "Modeler"
MIN_FIELDS = 3
MAX_FIELDS = 10


class CmdPrompt(Cmd):
    prompt = NAME + '> '
    intro = 'Welcome to the MODELER! Use ? command to list commands'

    gen = None
    tuple_list = TupleStore()

    def do_exit(self, _user_input):
        print("Exiting...")
        return True

    def do_use(self, user_input):
        model_object = fields = None

        if user_input == '1':
            model_object, fields = ("Python Package", ['Name', 'Author', 'Version', 'Description'])
        elif user_input == '2':
            model_object, fields = ("Fruit", ['Name', 'Colour', 'Flavour'])
        elif user_input == '3':
            model_object, fields = ("Code Editor", ['Name', 'Developer', 'Primary Language', 'Price'])
        else:
            print("Please select one of the following by using 'use 1' to use example 1.")
            print("1    [ Python Package ] -- (Name, Author, Version, Description)")
            print("2    [      Fruit     ] -- (Name, Colour, Flavour)")
            print("3    [  Code Editor   ] -- (Name, Developer, Primary Language, Price)")
            return

        self.__set_model(model_object, fields)
        print(Formatting.format("Setting %r as the model..." % model_object, Formatting.GREEN))

    def do_new(self, model_object):
        '''Creates a new model'''
        if model_object == "":
            # prompt for object
            model_object = prompt("Type of object")

        model_object = capitalise_str(model_object)

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

            field = capitalise_str(field)
            # prevent duplicate field names
            if field in fields:
                print(Formatting.error("A field with name %r already exists" % field))
                continue

            fields.append(field)
            i += 1

        print(Formatting.format("\n%s fields: " % model_object, [Formatting.BOLD, Formatting.GREEN])
              + "%s" % ', '.join(fields))

        self.__set_model(model_object, fields)

    def do_add(self, _user_input):
        '''Adds a new tuple to the store'''
        if not self.__has_model():
            return

        new_tuple = self.gen.new()
        self.tuple_list.append(new_tuple)

    def do_list(self, _user_input):
        # TODO: formatting
        self.tuple_list.print()

    def do_search(self, user_input):
        # TODO: find a tuple by search string
        if not self.__has_model():
            return

        if user_input == "":
            print(Formatting.error(
                "No search term provided.\nUse as 'search bob' where bob is the search term (case insensitive)."))
            return

        found: TupleStore = self.tuple_list.find_tuples(user_input)

        no_found = len(found)
        if no_found == 0:
            print(Formatting.error("No tuples were found with that search string :("))
        else:
            print(Formatting.format("Found %d tuple%s..." % (no_found, "s" if no_found > 1 else ""), Formatting.GREEN))
            found.print()

    def __has_model(self) -> bool:
        if self.gen is None:
            print(Formatting.error("No model set. Create one using the 'new' command."))
            return False
        return True

    def __set_model(self, object, fields):
        self.gen = TupleGen(object, fields)
        self.tuple_list = TupleStore(object=object)
        self.prompt = "%s (%s)> " % (NAME, object)


if __name__ == '__main__':
    CmdPrompt().cmdloop()
