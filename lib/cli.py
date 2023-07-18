from datetime import datetime
import click
from db.models import Gemstone, Practitioner, Member, Usage, Session
from sqlalchemy import or_

@click.group()
def cli():
    """Welcome to Spirit Stones, the Gemstone Management Application!"""


@click.command()
@click.option('--name', prompt='Name of the gemstone', help='The name of the gemstone.')
@click.option('--color', prompt='Color of the gemstone', help='The color of the gemstone.')
@click.option('--properties', prompt='Properties of the gemstone', help='The properties of the gemstone.')
def add_gemstone(name, color, properties):
    """Add a new gemstone to the collection."""
    session = Session()
    
    new_gemstone = Gemstone(name=name, color=color, properties=properties, availability=True)
    session.add(new_gemstone)
    
    session.commit()
    click.echo(f"Gemstone added with ID {new_gemstone.id}.")


@click.command()
@click.option('--id', prompt='ID of the gemstone to remove', help='The ID of the gemstone to remove.')
def remove_gemstone(id):
    """Remove a gemstone from the collection."""
    session = Session()
    
    gemstone = session.get(Gemstone, id)
    if gemstone is not None:
        session.delete(gemstone)
        session.commit()
        click.echo(f"Removed gemstone with ID {id}.")
    else:
        click.echo(f"No gemstone found with ID {id}.")


@click.command()
@click.option('--id', prompt='ID of the gemstone to update', help='The ID of the gemstone to update.')
@click.option('--name', prompt='New name of the gemstone', help='The new name of the gemstone.')
@click.option('--color', prompt='New color of the gemstone', help='The new color of the gemstone.')
@click.option('--properties', prompt='New properties of the gemstone', help='The new properties of the gemstone.')
def update_gemstone(id, name, color, properties):
    """Update a gemstone in the collection."""
    session = Session()
    
    gemstone = session.get(Gemstone, id)
    if gemstone is not None:
        gemstone.name = name
        gemstone.color = color
        gemstone.properties = properties
        session.commit()
        click.echo(f"Updated gemstone with ID {id}.")
    else:
        click.echo(f"No gemstone found with ID {id}.")


@click.command()
@click.option('--id', prompt='ID of the gemstone to view', help='The ID of the gemstone to view.')
def view_gemstone(id):
    """View a gemstone in the collection."""
    session = Session()
    
    gemstone = session.get(Gemstone, id)
    if gemstone is not None:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
    else:
        click.echo(f"No gemstone found with ID {id}.")


@click.command()
@click.option('--query', prompt='Search query', help='The search query.')
def search_gemstone(query):
    """Search for a gemstone in the collection."""
    session = Session()
    
    gemstones = session.query(Gemstone).filter(
        or_(Gemstone.name.contains(query), Gemstone.properties.contains(query))
    ).all()
    
    for gemstone in gemstones:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
        click.echo("-------")


@click.command()
@click.option('--gemstone_id', type=int, prompt='ID of the gemstone', help='The ID of the gemstone.')
@click.option('--practitioner_id', type=int, prompt='ID of the practitioner', help='The ID of the practitioner.')
@click.option('--member_id', type=int, prompt='ID of the member', help='The ID of the member.')
def add_usage(gemstone_id, practitioner_id, member_id):
    """Add a new usage record."""
    session = Session()
    
    new_usage = Usage(gemstone_id=gemstone_id, practitioner_id=practitioner_id, member_id=member_id, start_date=datetime.now())
    session.add(new_usage)
   
    gemstone = session.get(Gemstone, gemstone_id)
    gemstone.update_availability(session)

    session.commit()
    click.echo(f"Usage added with ID {new_usage.id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the usage to update', help='The ID of the usage to update.')
@click.option('--gemstone_id', type=int, prompt='New ID of the gemstone', help='The new ID of the gemstone.')
@click.option('--practitioner_id', type=int, prompt='New ID of the practitioner', help='The new ID of the practitioner.')
@click.option('--member_id', type=int, prompt='New ID of the member', help='The new ID of the member.')
@click.option('--end_date', prompt='New end date of the usage (YYYY-MM-DD)', help='The new end date of the usage.')
def update_usage(id, gemstone_id, practitioner_id, member_id, end_date):
    """Update a usage."""
    session = Session()
    
    usage = session.query(Usage).get(id)
    if usage is not None:
        usage.gemstone_id = gemstone_id
        usage.practitioner_id = practitioner_id
        usage.member_id = member_id
        usage.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        session.commit()
        click.echo(f"Updated usage with ID {id}.")
    else:
        click.echo(f"No usage found with ID {id}.")

    gemstone = session.get(Gemstone, gemstone_id)
    gemstone.update_availability(session)

    session.commit()
    click.echo(f"Usage updated.")


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
@click.option('--name', prompt='Name of the practitioner', help='The name of the practitioner.')
@click.option('--specialization', prompt='Specialization of the practitioner', help='The specialization of the practitioner.')
def add_practitioner(name, specialization):
    """Add a new practitioner."""
    session = Session()
    
    new_practitioner = Practitioner(name=name, specialization=specialization)
    session.add(new_practitioner)
    
    session.commit()
    click.echo(f"Practitioner added with ID {new_practitioner.id}.")


@click.command()
@click.option('--id', type=int, prompt='ID of the practitioner to update', help='The ID of the practitioner to update.')
@click.option('--name', prompt='New name of the practitioner', help='The new name of the practitioner.')
@click.option('--specialization', prompt='New specialization of the practitioner', help='The new specialization of the practitioner.')
def update_practitioner(id, name, specialization):
    """Update a practitioner."""
    session = Session()
    
    practitioner = session.get(Practitioner, id)
    if practitioner is not None:
        practitioner.name = name
        practitioner.specialization = specialization
        session.commit()
        click.echo(f"Updated practitioner with ID {id}.")
    else:
        click.echo(f"No practitioner found with ID {id}.")


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
@click.option('--id', type=int, prompt='ID of the practitioner to remove', help='The ID of the practitioner to remove.')
def remove_practitioner(id):
    """Remove a practitioner."""
    session = Session()
    
    practitioner = session.get(Practitioner, id)
    if practitioner is not None:
        session.delete(practitioner)
        session.commit()
        click.echo(f"Removed practitioner with ID {id}.")
    else:
        click.echo(f"No practitioner found with ID {id}.")


@click.command()
def list_gemstones():
    """List all gemstones in the collection."""
    session = Session()
    
    gemstones = session.query(Gemstone).all()
    
    for gemstone in gemstones:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
        click.echo("-------")


@click.command()
def list_practitioners():
    """List all practitioners."""
    session = Session()
    
    practitioners = session.query(Practitioner).all()
    
    for practitioner in practitioners:
        click.echo(f"ID: {practitioner.id}")
        click.echo(f"Name: {practitioner.name}")
        click.echo(f"Specialization: {practitioner.specialization}")
        click.echo("-------")


@click.command()
def list_members():
    """List all members."""
    session = Session()
    
    members = session.query(Member).all()
    
    for member in members:
        click.echo(f"ID: {member.id}")
        click.echo(f"Name: {member.name}")
        click.echo("-------")


cli.add_command(add_gemstone)
cli.add_command(update_gemstone)
cli.add_command(remove_gemstone)
cli.add_command(view_gemstone)
cli.add_command(search_gemstone)
cli.add_command(add_usage)
cli.add_command(update_usage)
cli.add_command(add_member)
cli.add_command(update_member)
cli.add_command(remove_member)
cli.add_command(add_practitioner)
cli.add_command(update_practitioner)
cli.add_command(remove_practitioner)
cli.add_command(list_gemstones)
cli.add_command(list_practitioners)
cli.add_command(list_members)

if __name__ == '__main__':
    cli()
