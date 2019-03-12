import delegator


def run_command(command):
    print("$ {command}".format(command=command))
    c = delegator.run(command)
    return c.out, c.return_code
