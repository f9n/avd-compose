import os
import sys
import functools

import click

from . import __version__
from .parser import parse_configuration_file
from .androidstudio.avdmanager import Avd
from .androidstudio import emulator
from .androidstudio import AndroidHome

DEFAULT_CONFIG_FILE = os.getenv("AVD_COMPOSE_CONFIG_FILE", "avd-compose.yml")


def get_platform_by_name(platforms, name):
    for platform in platforms:
        if platform["name"] == name:
            return platform

    message = "We didn't find this {name} platform name in configuration file".format(
        name=name
    )
    sys.exit(message)


def filter_platforms_by_name(platforms, name=None):
    if name is None:
        return platforms

    return get_platform_by_name(platforms, name)


def configuration_file_required(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        ctx = args[0]
        ctx.obj["configs"] = parse_configuration_file(ctx.obj["config_file"])
        return func(*args, **kwargs)

    return wrapper_decorator


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("-c", "--config-file", default=DEFAULT_CONFIG_FILE)
@click.pass_context
def main(ctx, debug, config_file):
    ctx.ensure_object(dict)

    ctx.obj["debug"] = debug
    ctx.obj["config_file"] = config_file


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
@configuration_file_required
@AndroidHome.required
def create(ctx, name):
    """ creates android virtual devices """
    platforms = ctx.obj["configs"]["platforms"]
    for platform in filter_platforms_by_name(platforms, name):
        stdout, stderr, rc = Avd.create(name=platform["name"], **platform["avd"])
        if ctx.obj["debug"]:
            click.echo(stdout)
            click.echo(stderr)
            click.echo(rc)


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", required=True, type=str, help="specific android virtual device name"
)
@configuration_file_required
@AndroidHome.required
def up(ctx, name):
    """ starts the avd-compose environment """
    platforms = ctx.obj["configs"]["platforms"]
    platform = get_platform_by_name(platforms, name)
    platform_emulator = platform["emulator"] or {}
    stdout, stderr, rc = emulator.start(name=platform["name"], **platform_emulator)
    if ctx.obj["debug"]:
        click.echo(stdout)
        click.echo(stderr)
        click.echo(rc)


@main.command()
@click.pass_context
@configuration_file_required
def status(ctx):
    """ status of the android virtual devices in the configuration file """
    platforms = ctx.obj["configs"]["platforms"]
    for platform in platforms:
        click.echo(platform["name"])


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
@configuration_file_required
@AndroidHome.required
def destroy(ctx, name):
    """ deletes all the android virtual devices """
    platforms = ctx.obj["configs"]["platforms"]
    for platform in filter_platforms_by_name(platforms, name):
        stdout, stderr, rc = Avd.delete(name=platform["name"])
        if ctx.obj["debug"]:
            click.echo(stdout)
            click.echo(stderr)
            click.echo(rc)


if __name__ == "__main__":
    main(obj={})
