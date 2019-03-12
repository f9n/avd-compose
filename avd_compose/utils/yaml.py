import io

import yaml as y


def load_file(filepath):
    with io.open(filepath, "r") as f:
        return y.load(f)
