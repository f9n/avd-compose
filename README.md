# avd-compose [![PyPi version](https://img.shields.io/pypi/v/avd-compose.svg)](https://pypi.python.org/pypi/avd-compose/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/avd-compose.svg)](https://pypi.python.org/pypi/avd-compose/) [![](https://img.shields.io/github/license/f9n/avd-compose.svg)](https://github.com/f9n/avd-compose/blob/master/LICENSE)

Define and run android virtual devices

# Install

```bash
$ pip3 install --user avd-compose
```

# Usage

```bash
$ avd-compose --help
$ avd-compose version
$ cat <<EOF >avd-compose.yml
version: 1

platforms:
  - name: My_Nexus_5
    avd:
      package: "system-images;android-27;google_apis_playstore;x86"
      device: Nexus 5
    emulator:

  - name: My_Nexus_One
    avd:
      package: "system-images;android-27;google_apis_playstore;x86"
      device: Nexus One
    emulator:

EOF
$ # Create all of them
$ avd-compose create
$ # Create one of them
$ avd-compose create --name My_Nexus_One
$ # Destroy all of them
$ avd-compose destroy
$ # Destroy one of them
$ avd-compose destroy --name My_Nexus_One
$ avd-compose up --name My_Nexus_5
```

# Examples

Look up the [examples](https://github.com/f9n/avd-compose/tree/master/examples) directory.

# Credits

- [Docker Compose](https://github.com/docker/compose)
- [Vagrant](https://github.com/hashicorp/vagrant)
