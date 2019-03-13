import sys

import delegator


def get_full_path(tool):
    command = "which {tool}".format(tool=tool)
    c = delegator.run(command)
    if not c.return_code == 0:
        sys.exit("We can't find the full path for this '{tool}' tool".format(tool=tool))

    return c.out


class Emulator:
    @staticmethod
    def full_path():
        return get_full_path("emulator").strip()

    @staticmethod
    def start(name):
        command = "{full_path_of_tool} -avd {name}".format(
            full_path_of_tool=Emulator.full_path(), name=name
        )
        print("$ {command}".format(command=command))
        c = delegator.run(command)
        return c.out, c.err, c.return_code

