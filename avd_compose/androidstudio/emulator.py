import delegator

from ..utils import shell


class Emulator:
    @staticmethod
    def __full_path():
        return shell.get_full_path("emulator").strip()

    @staticmethod
    def start(name):
        command = "{full_path_of_tool} -avd {name}".format(
            full_path_of_tool=Emulator.__full_path(), name=name
        )
        return shell.run_command(command=command)

