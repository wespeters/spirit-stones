import click
from db.models import Gemstone, Session
from sqlalchemy import or_

@click.group()
def cli():
    pass


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

cli.add_command(add_gemstone)


@click.command()
@click.option('--id', prompt='ID of the gemstone to remove', help='The ID of the gemstone to remove.')
def remove_gemstone(id):
    """Remove a gemstone from the collection."""
    session = Session()
    
    gemstone = session.query(Gemstone).get(id)
    if gemstone is not None:
        session.delete(gemstone)
        session.commit()
        click.echo(f"Removed gemstone with ID {id}.")
    else:
        click.echo(f"No gemstone found with ID {id}.")

cli.add_command(remove_gemstone)


@click.command()
@click.option('--id', prompt='ID of the gemstone to update', help='The ID of the gemstone to update.')
@click.option('--name', prompt='New name of the gemstone', help='The new name of the gemstone.')
@click.option('--color', prompt='New color of the gemstone', help='The new color of the gemstone.')
@click.option('--properties', prompt='New properties of the gemstone', help='The new properties of the gemstone.')
def update_gemstone(id, name, color, properties):
    """Update a gemstone in the collection."""
    session = Session()
    
    gemstone = session.query(Gemstone).get(id)
    if gemstone is not None:
        gemstone.name = name
        gemstone.color = color
        gemstone.properties = properties
        session.commit()
        click.echo(f"Updated gemstone with ID {id}.")
    else:
        click.echo(f"No gemstone found with ID {id}.")

cli.add_command(update_gemstone)


@click.command()
@click.option('--id', prompt='ID of the gemstone to view', help='The ID of the gemstone to view.')
def view_gemstone(id):
    """View a gemstone in the collection."""
    session = Session()
    
    gemstone = session.query(Gemstone).get(id)
    if gemstone is not None:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
    else:
        click.echo(f"No gemstone found with ID {id}.")

cli.add_command(view_gemstone)


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


cli.add_command(add_gemstone)
cli.add_command(remove_gemstone)
cli.add_command(update_gemstone)
cli.add_command(view_gemstone)
cli.add_command(search_gemstone)

if __name__ == '__main__':
    cli()
