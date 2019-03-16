import delegator

from ..utils import shell, formatter
from . import Tools


def full_path():
    return Tools.get_full_path("emulator")


def start(name, **kwargs):
    options_string = formatter.options_as_a_string(kwargs, option_prefix="-")
    command = "{full_path_of_tool} -avd {name} {options}".format(
        full_path_of_tool=full_path(), name=name, options=options_string
    )
    return shell.run_command(command=command)

