"""
Modelling a python package

Name, Author, Version, Description
"""

from cmd import Cmd

from tuple import TupleGen

TUPLE_LIST = []

gen = TupleGen("Package", ['NAME', 'AUTHOR', 'VERSION', 'DESCRIPTION'])


class CmdPrompt(Cmd):
    prompt = 'Modeler> '
    intro = 'Welcome to the MODELER! Use ? command to list commands'

    def do_exit(self, input):
        print("Exiting...")
        return True

    def do_new(self, input):
        '''Creates a new model'''
        if input == "":
            # TODO: prompt for object
            pass

        # TODO: prompt for field list

    def do_add(self, input):
        '''Adds a new tuple to the store'''
        add_tuple(gen)

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
