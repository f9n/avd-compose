from ..utils import shell


class Avd:
    @staticmethod
    def __full_path():
        return shell.get_full_path("avdmanager").strip()

    @staticmethod
    def create(name, package, device, force=True):
        # If this package is not available in the system, you should install the package with 'sdkmanager'.
        command = """{full_path_of_tool} create avd --name "{name}" --package "{package}" --device "{device}" --force""".format(
            full_path_of_tool=Avd.__full_path(),
            name=name,
            package=package,
            device=device,
        )
        return shell.run_command(command)

    @staticmethod
    def delete(name):
        command = """{full_path_of_tool} delete avd --name "{name}" """.format(
            full_path_of_tool=Avd.__full_path(), name=name
        )
        return shell.run_command(command)

    @staticmethod
    def move(name, rename, path):
        pass

    @staticmethod
    def list():
        command = "{full_path_of_tool} list avd".format(
            full_path_of_tool=Avd.__full_path()
        )
        return shell.run_command(command)


class Target:
    @staticmethod
    def list():
        command = "{full_path_of_tool} list target".format(
            full_path_of_tool=Avd.__full_path()
        )
        return shell.run_command(command)


class Device:
    @staticmethod
    def list():
        command = "{full_path_of_tool} list device".format(
            full_path_of_tool=Avd.__full_path()
        )
        return shell.run_command(command)
