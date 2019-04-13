import click

from chaos_loader.utils.error_handler import modify_usage_error
from datasync.commands.configure import command as configure
from datasync.commands.terraform import command as terraform_commands
from datasync.commands.university import command as university_commands
from datasync.utils.decorators.common import global_options
from datasync.commands.heroku.command import heroku


@click.group()
@global_options
def cli(debug, quiet):
    pass


@click.command()
@click.argument('output', nargs=1)
@click.pass_context
def run(context, output):
    """RUN ALL"""
    # Generate clients json file
    context.invoke(university_commands.generate, output=output)
    # Generate cookie cutter template
    context.invoke(terraform_commands.generate, output=output)


"""
Add new commands here
"""
cli.add_command(terraform_commands.terraform)
cli.add_command(university_commands.university)
cli.add_command(configure.configure)
cli.add_command(heroku)
cli.add_command(run)

"""
Modify error handler
"""
modify_usage_error(cli)
