#!/usr/bin/python3
"""console airbnb"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console AIRBNB"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the console\n"""
        return True

    def emptyline(self):
        """ Empty Line  """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
