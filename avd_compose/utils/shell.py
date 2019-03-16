import sys

import delegator


def run_command(command):
    print("$ {command}".format(command=command))
    c = delegator.run(command)
    if not c.err == 0:
        sys.exit(c.err)

    return c.out, c.err, c.return_code

