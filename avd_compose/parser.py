import sys

from .utils import yaml


def check_missing_keys_in_dictionary(dictionary, required_fields):
    missing_fields = []
    for required_field in required_fields:
        if not dictionary.get(required_field):
            missing_fields.append(required_field)

    return missing_fields


# TODO:: Refactor
def validate_configuration_file(configs):
    messages = []
    avd_required_fields = ["package", "device"]
    for platform in configs["platforms"]:
        name = platform["name"]
        # Check avd field
        missing_fields = check_missing_keys_in_dictionary(
            platform["avd"], avd_required_fields
        )
        if missing_fields:
            messages.append(
                "Missing fields in avd section of '{name}' platform:\n{fields}".format(
                    name=name, fields=", ".join(missing_fields)
                )
            )

    if messages:
        sys.exit("\n".join(messages))


# TODO:: Refactor
def parse_configuration_file(config_filepath):
    try:
        content = yaml.load_file(config_filepath)
        validate_configuration_file(content)
        return content
    except Exception as e:
        sys.exit(e)
