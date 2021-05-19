"""
Modelling a python package

Name, Author, Version, Description
"""

from cmd import Cmd

from gen import Generator
from gen.class_gen import ClassGen
from storage import Store
from storage.class_store import ClassStore
from storage.tuple_store import TupleStore
from utils import Formatting, format_model_name, prompt
from gen.tuple_gen import TupleGen

NAME = "Modeler"
MIN_FIELDS = 3
MAX_FIELDS = 10

store_class: Store.__class__ = None
gen_class: Generator.__class__ = None


class CmdPrompt(Cmd):
    prompt = NAME + '> '
    intro = 'Welcome to the MODELER! Use ? command to list commands'

    gen = None

    # TODO: Set store
    store = None

    def do_exit(self, _user_input):
        print("Exiting...")
        return True

    def do_use(self, user_input):
        model_object = fields = None

        if user_input == '1':
            model_object, fields = ("PythonPackage", ['Name', 'Author', 'Version', 'Description'])
        elif user_input == '2':
            model_object, fields = ("Fruit", ['Name', 'Colour', 'Flavour'])
        elif user_input == '3':
            model_object, fields = ("CodeEditor", ['Name', 'Developer', 'Primary Language', 'Price'])
        else:
            print("Please select one of the following by using 'use 1' to use example 1.")
            print("1    [ PythonPackage ] -- (Name, Author, Version, Description)")
            print("2    [      Fruit     ] -- (Name, Colour, Flavour)")
            print("3    [  CodeEditor   ] -- (Name, Developer, Primary Language, Price)")
            return

        self.__set_model(model_object, fields)
        print(Formatting.format("Setting %r as the model..." % model_object, Formatting.GREEN))

    def do_new(self, model_object):
        '''Creates a new model'''
        if model_object == "":
            # prompt for object
            model_object = prompt("Type of object")

        model_object = format_model_name(model_object)

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

            field = format_model_name(field)
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

        new_item = self.gen.new()
        self.store.append(new_item)

    def do_list(self, _user_input):
        self.store.print()

    def do_search(self, user_input):
        if not self.__has_model():
            return

        if user_input == "":
            print(Formatting.error(
                "No search term provided.\nUse as 'search bob' where bob is the search term (case insensitive)."))
            return

        found: store_class = self.store.search(user_input)

        no_found = len(found)
        if no_found == 0:
            print(Formatting.error("No items were found with that search string :("))
        else:
            print(Formatting.format("Found %d item%s..." % (no_found, "s" if no_found > 1 else ""), Formatting.GREEN))
            found.print()

    def __has_model(self) -> bool:
        if self.gen is None or self.store is None:
            print(Formatting.error("No model set. Create one using the 'new' command."))
            return False
        return True

    def __set_model(self, object, fields):
        self.gen = gen_class(object, fields)
        self.store = store_class(object=object)

        self.prompt = "%s (%s)> " % (NAME, object)


if __name__ == '__main__':
    while True:
        print("How would you like to store models? (1) Tuples or (2) Classes")
        choice = input("Storage Method: ")
        if choice == '1':
            store_class = TupleStore
            gen_class = TupleGen
            break
        elif choice == '2':
            store_class = ClassStore
            gen_class = ClassGen
            break
        # Otherwise keeps asking

    CmdPrompt().cmdloop()
