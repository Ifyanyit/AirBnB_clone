#!/usr/bin/python3
"""
Console: Entry point of the command interpreter
"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ cmd clone"""
    intro = 'Welcome to the Airbnb console. Type help or ? to list commands.\n'
    prompt = '(hbnb) '


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit console"""
        return True

    def emptyline(self):
        """empty line. Do nothing"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
