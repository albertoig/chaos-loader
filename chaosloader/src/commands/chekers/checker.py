import click

from datasync.utils.decorators.common import global_options


@click.command()
@click.pass_context
@global_options
def apply(context, debug, quiet):
    """This statement will generate a json organizations file."""
    click.echo("command apply works!")
