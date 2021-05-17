"""
Modelling a python package

Name, Author, Version, Description
"""

from cmd import Cmd

from prompt import prompt
from tuple import TupleGen

MIN_FIELDS = 3
MAX_FIELDS = 10

TUPLE_LIST = []


class CmdPrompt(Cmd):
    prompt = 'Modeler> '
    intro = 'Welcome to the MODELER! Use ? command to list commands'

    gen = None

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

            fields.append(field.upper())
            i += 1

        print("%s fields: %s" % (object, ', '.join(fields)))

        self.gen = TupleGen(object, fields)


    def do_add(self, input):
        '''Adds a new tuple to the store'''
        if self.gen == None:
            print("No model set. Set using the 'new' command.")
            return

        add_tuple(self.gen)

    def do_list(self, input):
        # TODO: formatting
        print(TUPLE_LIST)

    def do_search(self, input):
        # TODO: find a tuple by search string
        if input == "":
            print("No search term provided.\nUse as 'search bob' where bob is the search term (case insensitive).")
            return

        if len(TUPLE_LIST) == 0:
            print("No tuples stored. Please add one using the 'add' command.")
            return


def add_tuple(gen):
    new_tuple = gen.new()
    TUPLE_LIST.append(new_tuple)


if __name__ == '__main__':
    CmdPrompt().cmdloop()
