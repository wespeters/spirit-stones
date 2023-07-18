import click
from gemstones import commands as gemstone_commands
from members import commands as member_commands
from practitioners import commands as practitioner_commands
from usages import commands as usage_commands


@click.group()
def cli():
    """Welcome to Spirit Stones, the Gemstone Management Application!"""


for command in gemstone_commands + member_commands + practitioner_commands + usage_commands:
    cli.add_command(command)


if __name__ == '__main__':
    cli()
