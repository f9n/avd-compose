from ..utils import shell


class Avd:
    @staticmethod
    def create(name, package, device, force=True):
        # If this package is not available in the system, you should install the package with 'sdkmanager'.
        command = """avdmanager create avd --name {name} --package "{package}" --device "{device}" --force""".format(
            name=name, package=package, device=device
        )
        return shell.run_command(command)

    @staticmethod
    def delete(name):
        command = "avdmanager delete avd --name {name}".format(name=name)
        return shell.run_command(command)

    @staticmethod
    def move(name, rename, path):
        pass

    @staticmethod
    def list():
        command = "avdmanager list avd"
        return shell.run_command(command)


class Target:
    @staticmethod
    def list():
        command = "avdmanager list target"
        return shell.run_command(command)


class Device:
    @staticmethod
    def list():
        command = "avdmanager list device"
        return shell.run_command(command)
