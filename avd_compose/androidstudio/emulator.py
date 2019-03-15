import delegator

from ..utils import shell, formatter


class Emulator:
    @staticmethod
    def __full_path():
        return shell.get_full_path("emulator").strip()

    @staticmethod
    def start(name, **kwargs):
        options_string = formatter.options_as_a_string(kwargs)
        command = "{full_path_of_tool} -avd {name} {options}".format(
            full_path_of_tool=Emulator.__full_path(), name=name, options=options_string
        )
        return shell.run_command(command=command)

