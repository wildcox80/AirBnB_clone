#!/usr/bin/python3
"""console airbnb"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console AIRBNB"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the console\n"""
        return True

    def do_help(self, arg):
        """Help command to get info on specified command
        If no parameter given, list all commands
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """ Empty Line  """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
