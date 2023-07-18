import click
from db.models import Session, Member


@click.command()
@click.option('--name', prompt='Name of the member', help='The name of the member.')
def add_member(name):
    """Add a new member."""
    session = Session()
    
    new_member = Member(name=name)
    session.add(new_member)
    
    session.commit()
    click.echo(f"Member added with ID {new_member.id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the member to update', help='The ID of the member to update.')
@click.option('--name', prompt='New name of the member', help='The new name of the member.')
def update_member(id, name):
    """Update a member."""
    session = Session()
    
    member = session.get(Member, id)
    if member is not None:
        member.name = name
        session.commit()
        click.echo(f"Updated member with ID {id}.")
    else:
        click.echo(f"No member found with ID {id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the member to remove', help='The ID of the member to remove.')
def remove_member(id):
    """Remove a member."""
    session = Session()
    
    member = session.get(Member, id)
    if member is not None:
        session.delete(member)
        session.commit()
        click.echo(f"Removed member with ID {id}.")
    else:
        click.echo(f"No member found with ID {id}.")


@click.command()
def list_members():
    """List all members."""
    session = Session()
    
    members = session.query(Member).all()
    
    for member in members:
        click.echo(f"ID: {member.id}")
        click.echo(f"Name: {member.name}")
        click.echo("-------")


commands = [add_member, remove_member, update_member, list_members]