import os

import click

from . import __version__
from .parser import parse_configuration_file
from .androidstudio.avdmanager import Avd

DEFAULT_CONFIG_FILE = os.getenv("AVD_COMPOSE_CONFIG_FILE", "avd-compose.yml")


def get_platforms_by_name(platforms, name=None):
    for platform in platforms:
        if name and not platform["name"] == name:
            continue

        yield platform


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("-c", "--config-file", default=DEFAULT_CONFIG_FILE)
@click.pass_context
def main(ctx, debug, config_file):
    ctx.ensure_object(dict)

    ctx.obj["debug"] = debug
    ctx.obj["configs"] = parse_configuration_file(config_file)


@main.command()
@click.pass_context
def version(ctx):
    """ prints the avd-compose, avdmanager, sdkmanager, emulator versions """
    click.echo("avd-compose {version}".format(version=__version__))


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
def create(ctx, name):
    """ creates android virtual devices """
    platforms = ctx.obj["configs"]["platforms"]
    for platform in get_platforms_by_name(platforms, name):
        output, return_code = Avd.create(
            name=platform["name"],
            package=platform["avd"]["package"],
            device=platform["avd"]["device"],
        )
        if ctx.obj["debug"]:
            click.echo(output)
            click.echo(return_code)


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
def up(ctx, name):
    """ starts the avd-compose environment """
    pass


@main.command()
@click.pass_context
def status(ctx):
    """ status of the android virtual devices in the configuration file """
    pass


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
def destroy(ctx, name):
    """ deletes all the android virtual devices """
    platforms = ctx.obj["configs"]["platforms"]
    for platform in get_platforms_by_name(platforms, name):
        output, return_code = Avd.delete(name=platform["name"])
        if ctx.obj["debug"]:
            click.echo(output)
            click.echo(return_code)


if __name__ == "__main__":
    main(obj={})
