import sys

import delegator


def run_command(command):
    print("$ {command}".format(command=command))
    c = delegator.run(command)
    return c.out, c.err, c.return_code


def get_full_path(tool):
    command = "which {tool}".format(tool=tool)
    c = delegator.run(command)
    if not c.return_code == 0:
        sys.exit("We can't find the full path for this '{tool}' tool".format(tool=tool))

    return c.out
