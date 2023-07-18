import click
from db.models import Session, Gemstone
from sqlalchemy import or_

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
@click.option('--query', prompt='Search for a gemstone by name, color, or properties', help='The search query.')
def search_gemstone(query):
    """Search for a gemstone in the collection."""
    session = Session()
    
    gemstones = session.query(Gemstone).filter(
        or_(Gemstone.name.contains(query), Gemstone.properties.contains(query), 
            Gemstone.color.contains(query), Gemstone.id.contains(query))
    ).all()
    
    for gemstone in gemstones:
        click.echo(f"ID: {gemstone.id}")
        click.echo(f"Name: {gemstone.name}")
        click.echo(f"Color: {gemstone.color}")
        click.echo(f"Properties: {gemstone.properties}")
        click.echo(f"Availability: {'Available' if gemstone.availability else 'Not Available'}")
        click.echo("-------")


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


commands = [add_gemstone, remove_gemstone, update_gemstone, view_gemstone, search_gemstone, list_gemstones]
