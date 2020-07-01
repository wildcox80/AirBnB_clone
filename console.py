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

    def do_create(self, line):
        """Create a instance of a AirBnb class"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            if line:
                new_obj_id = eval(line + "()")
                new_obj_id.save()
                print(new_obj_id.id)
            else:
                print("** class doesn't exist **")
                return

    def do_all(self, line):
        """ Print all instances in string representation """
        objects = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])

        else:
            st = line.split(" ")
            if st[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == st[0]:
                        objects.append(str(value))
                print(objects)

    def emptyline(self):
        """ Empty Line  """
        pass

    def do_show(self, line):
        """ command show """
        try:
            if line is None or line == "":
                raise SyntaxError()
            else:
                st = line.split(" ")
                if st[0] not in self.classes:
                    raise NameError()
                if len(st) < 2:
                    raise IndexError()
                key = "{}.{}".format(st[0], st[1])
                obs = storage.all()
                if key in obs:
                    print(obs[key])
                else:
                    raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """ Function that destroy the instance """
        try:
            if line is None or line == "":
                raise SyntaxError()
            else:
                st = line.split(" ")
                if st[0] not in self.classes:
                    raise NameError()
                if len(st) < 2:
                    raise IndexError()
                else:
                    ob_sto = storage.all()
                    obs = "{}.{}".format(st[0], st[1])
                    if obs in ob_sto:
                        del (ob_sto[obs])
                        storage.save()
                    else:
                        raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_update(self, line):
        """ Updates instance """
        try:
            if not line:
                raise SyntaxError()
            line_split = line.split(" ")
            if line_split[0] not in self.classes:
                raise NameError()
            if len(line_split) < 2:
                raise IndexError()
            dic = storage.all()
            k = "{}.{}".format(line_split[0], line_split[1])
            if k not in dic:
                raise KeyError()
            if len(line_split) < 3:
                raise AttributeError()
            if len(line_split) < 4:
                raise ValueError()
            objs = dic[k]
            try:
                objs.__dict__[line_split[2]] = eval(line_split[3])
                objs.save()
            except Exception:
                objs.__dict__[line_split[2]] = line_split[3]
                objs.save()
        except ValueError:
            print("** value missing **")
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
