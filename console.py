#!/usr/bin/python3
"""
    BnB interpreter programm
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Commandline class """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n """
        sys.exit()


    def do_EOF(self, line):
        """ handle EOF """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
