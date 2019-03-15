import sys


def validate(configs):
    messages = []
    avd_required_fields = ["package", "device"]
    for platform in configs["platforms"]:
        name = platform["name"]
        # Check platform avd field
        missing_fields = avd_required_fields - platform["avd"].keys()
        if missing_fields:
            messages.append(
                "Missing fields in avd section of '{name}' platform:\n{fields}".format(
                    name=name, fields=", ".join(missing_fields)
                )
            )

    if messages:
        sys.exit("\n".join(messages))
