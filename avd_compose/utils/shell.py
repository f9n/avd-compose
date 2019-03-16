import sys

import delegator


def run_command(command):
    print("$ {command}".format(command=command))
    c = delegator.run(command)
    return c.out, c.err, c.return_code

