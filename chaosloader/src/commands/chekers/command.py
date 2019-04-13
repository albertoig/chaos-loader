import click

from datasync.commands.terraform.generate import generate
from datasync.commands.terraform.apply import apply
from datasync.utils import chekers
from datasync.utils.decorators.common import global_options

TERRAFORM_CLI = 'terraform'


@click.group()
@click.pass_context
@global_options
def terraform(context, debug, quiet):
    """Terraform commands"""
    chekers.check_external_cli(context=context, name=TERRAFORM_CLI, debug=debug)
    pass


terraform.add_command(apply)
terraform.add_command(generate)
