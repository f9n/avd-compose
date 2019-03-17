import io
import sys

import yaml as y


def load_file(filepath):
    try:
        with io.open(filepath, "r") as f:
            return y.safe_load(f)
    except Exception as e:
        sys.exit(e)

