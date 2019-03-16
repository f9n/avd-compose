from ..utils import shell
from . import Tools


def full_path():
    return Tools.get_full_path("sdkmanager")


def install(package):
    command = """{full_path_of_tool} --install "{package}" """.format(
        full_path_of_tool=full_path(), package=package
    )
    return shell.run_command(command)
