"""

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
    prompt = Formatting.format(NAME + '> ', Formatting.BOLD)
    intro = Formatting.format("\nWelcome to the %s!\n" % NAME,
                              [Formatting.GREEN, Formatting.BOLD]) + \
            "Use ? command to list commands.\nBefore adding items, you must create a model using the 'new' command.\n" \
            "You can use some example models by using the 'use' command."

    gen = None

    # TODO: Set store
    store = None

    def do_exit(self, _user_input):
        """
        Exits the program.

        Arguments
            None

        Examples
            > exit
            Exiting...
            0
        """
        print(Formatting.error("Exiting..."))
        return True

    def do_use(self, user_input):
        """
        Uses an example model.

        Arguments
            - Model number

        Examples
            > use 1
            Setting 'PythonPackage' as the model...

        Options
            1    [ PythonPackage ] -- (Name, Author, Version, Description)
            2    [      Fruit     ] -- (Name, Colour, Flavour)
            3    [  CodeEditor   ] -- (Name, Developer, Primary Language, Price)
        """
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
        """
        Creates a new model.

        Must have at least 3 fields. Enter the field name 'q' to exit input

        Arguments
            - Name (Optional, will be prompted)

        Examples
            > new
            Model Name: Abc
            Field 1 name: a
            ...

            > new Abc
            Field 1 name: a
            ...
        """

        if model_object == "":
            # prompt for object
            model_object = prompt("Model Name")

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
        """
        Adds an item to the storage.

        Must have a model set.

        Arguments
            None

        Examples
            > add
            ---------[ New PythonPackage ]---------
            Name: a
            Author: b
            Version: c
            Description: d

            ~~>  PythonPackage(Name='a', Author='b', Version='c', Description='d')
        """
        if not self.__has_model():
            return

        new_item = self.gen.new()
        self.store.append(new_item)

    def do_list(self, _user_input):
        """
        Prints the items in the store.

        Must have a model set and items in the store.

        Arguments
            None

        Examples
            > list
            --------[ Printing Class Items ]--------
            ~~>  PythonPackage(Name='a', Author='b', Version='c', Description='d')
            -----------------------------------
        """
        self.store.print()

    def do_search(self, user_input):
        """
        Searches for items with query.

        Searches by checking if any attributes in the model starts with the query string.

        Must have a model set and items in the store.

        Arguments
            - query

        Examples
            > search bob
            Found 1 item...
            --------[ Printing Class Items ]--------
            ~~>  PythonPackage(Name='a', Author='bob', Version='c', Description='d')
            -----------------------------------
        """
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

        self.prompt = Formatting.format("%s " % NAME, Formatting.BOLD) +\
                      Formatting.format("(%s)" % object, [Formatting.BOLD, Formatting.PURPLE]) + \
                      Formatting.format("> ", Formatting.BOLD)


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
