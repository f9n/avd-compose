import delegator

from ..utils.shell import get_full_path


class Emulator:
    @staticmethod
    def __full_path():
        return get_full_path("emulator").strip()

    @staticmethod
    def start(name):
        command = "{full_path_of_tool} -avd {name}".format(
            full_path_of_tool=Emulator.__full_path(), name=name
        )
        print("$ {command}".format(command=command))
        c = delegator.run(command)
        return c.out, c.err, c.return_code
