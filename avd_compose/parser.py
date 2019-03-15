import sys

from .configs import v1
from .utils import yaml

# TODO:: Refactor
def validate_configuration_file(configs):
    config_version = configs["version"]
    if config_version == 1:
        return v1.validate(configs=configs)
    else:
        sys.exit(
            "We dont support this {config_version} version".format(
                config_version=config_version
            )
        )


# TODO:: Refactor
def parse_configuration_file(config_filepath):
    content = yaml.load_file(config_filepath)
    validate_configuration_file(content)
    return content
