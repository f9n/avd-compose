from .utils import yaml


def validate():
    pass


def parse_configuration_file(config_filepath):
    content = yaml.load_file(config_filepath)
    return content
