import sys

from .utils import yaml


def validate():
    pass


def parse_configuration_file(config_filepath):
    try:
        content = yaml.load_file(config_filepath)
        return content
    except Exception as e:
        sys.exit(e)
