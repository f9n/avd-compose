from ..utils import shell


class Sdk:
    @staticmethod
    def install(package):
        command = """sdkmanager --install "{package}" """.format(package=package)
        return shell.run_command(command)
