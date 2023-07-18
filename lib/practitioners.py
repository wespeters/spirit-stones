import click
from db.models import Session, Practitioner

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
def list_practitioners():
    """List all practitioners."""
    session = Session()
    
    practitioners = session.query(Practitioner).all()
    
    for practitioner in practitioners:
        click.echo(f"ID: {practitioner.id}")
        click.echo(f"Name: {practitioner.name}")
        click.echo(f"Specialization: {practitioner.specialization}")
        click.echo("-------")


commands = [add_practitioner, remove_practitioner, update_practitioner, list_practitioners]
