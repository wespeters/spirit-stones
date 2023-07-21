import click
from gemstones import commands as gemstone_commands
from members import commands as member_commands
from practitioners import commands as practitioner_commands
from usages import commands as usage_commands

def gemstone_submenu():
    click.echo('Gemstone commands:')
    click.echo('1. Add gemstone')
    click.echo('2. Remove gemstone')
    click.echo('3. Update gemstone')
    click.echo('4. View Gemstone')
    click.echo('5. Search Gemstones')
    click.echo('6. List Gesmstones')
    click.echo('7. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 7:
        return
    elif 1 <= choice <= 6:
        gemstone_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

def practitioner_submenu():
    click.echo('Practitioner commands:')
    click.echo('1. Add practitioner')
    click.echo('2. Remove practitioner')
    click.echo('3. Update practitioner')
    click.echo('4. List practitioners')
    click.echo('5. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 5:
        return
    elif 1 <= choice <= 4:
        practitioner_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

def member_submenu():
    click.echo('Member commands:')
    click.echo('1. Add member')
    click.echo('2. Remove member')
    click.echo('3. Update member')
    click.echo('4. List members')
    click.echo('5. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 5:
        return
    elif 1 <= choice <= 4:
        member_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

def usage_submenu():
    click.echo('Usage commands:')
    click.echo('1. Add usage')
    click.echo('2. Remove usage')
    click.echo('3. Update usage')
    click.echo('4. List usages')
    click.echo('5. Return to main menu')
    
    choice = click.prompt('Please enter your choice', type=str)

    try:
        choice = int(choice)
    except ValueError:
        click.echo('Invalid choice. Please choose a valid option.')
        return
    
    if choice == 5:
        return
    elif 1 <= choice <= 4:
        usage_commands[choice - 1]()
    else:
        click.echo('Invalid choice. Please choose a valid option.')

@click.group()
def cli():
    """Welcome to Spirit Stones, the Gemstone Management Application!"""

if __name__ == '__main__':
    while True:
        click.echo('Main menu:')
        click.echo('1. Gemstone commands')
        click.echo('2. Member commands')
        click.echo('3. Practitioner commands')
        click.echo('4. Usage commands')
        click.echo('q. Quit')

        choice = click.prompt('Please enter your choice', type=str)

        if choice == '1':
            gemstone_submenu()
        elif choice == '2':
            member_submenu()
        elif choice == '3':
            practitioner_submenu()
        elif choice == '4':
            usage_submenu()
        elif choice.lower() == 'q':
            break
        else:
            click.echo('Invalid choice. Please choose a valid option.')

for command in gemstone_commands + member_commands + practitioner_commands + usage_commands:
    cli.add_command(command)
