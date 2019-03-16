import sys

from ..utils import shell, formatter
from . import Tools, sdkmanager


def full_path():
    return Tools.get_full_path("avdmanager")


class Avd:
    @staticmethod
    def create(name, **kwargs):
        # If this package is not available in the system, you should install the package with 'sdkmanager'.
        sdkmanager.install(package=kwargs["package"])

        options_string = formatter.options_as_a_string(kwargs)
        command = """{full_path_of_tool} create avd --name "{name}" {options}""".format(
            full_path_of_tool=full_path(), name=name, options=options_string
        )
        return shell.run_command(command)

    @staticmethod
    def delete(name):
        command = """{full_path_of_tool} delete avd --name "{name}" """.format(
            full_path_of_tool=full_path(), name=name
        )
        return shell.run_command(command)

    @staticmethod
    def move(name, rename, path):
        pass

    @staticmethod
    def list():
        command = "{full_path_of_tool} list avd".format(full_path_of_tool=full_path())
        return shell.run_command(command)


class Target:
    @staticmethod
    def list():
        command = "{full_path_of_tool} list target".format(
            full_path_of_tool=full_path()
        )
        return shell.run_command(command)


class Device:
    @staticmethod
    def list():
        command = "{full_path_of_tool} list device".format(
            full_path_of_tool=full_path()
        )
        return shell.run_command(command)
