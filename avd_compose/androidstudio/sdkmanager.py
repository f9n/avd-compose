from ..utils import shell


class Sdk:
    @staticmethod
    def __full_path():
        return shell.get_full_path("sdkmanager").strip()

    @staticmethod
    def install(package):
        command = """{full_path_of_tool} --install "{package}" """.format(
            full_path_of_tool=Sdk.__full_path(), package=package
        )
        return shell.run_command(command)
