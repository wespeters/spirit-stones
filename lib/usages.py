import click
from datetime import datetime
from db.models import Session, Usage, Gemstone


@click.command()
@click.option('--gemstone_id', type=int, prompt='ID of the gemstone', help='The ID of the gemstone.')
@click.option('--practitioner_id', type=int, prompt='ID of the practitioner', help='The ID of the practitioner.')
@click.option('--member_id', type=int, prompt='ID of the member', help='The ID of the member.')
def add_usage(gemstone_id, practitioner_id, member_id):
    """Add a new usage record."""
    session = Session()
    
    gemstone = session.get(Gemstone, gemstone_id)

    if gemstone is None:
        click.echo(f"Error: No gemstone found with ID {gemstone_id}.")
        return
    elif not gemstone.availability:
        click.echo(f"Gemstone with ID {gemstone_id} is not available.")
        return
    
    new_usage = Usage(gemstone_id=gemstone_id, practitioner_id=practitioner_id, member_id=member_id, start_date=datetime.now())
    session.add(new_usage)
   
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
@click.option('--id', prompt='ID of the usage to remove', help='The ID of the usage to remove.')
def remove_usage(id):
    """Remove a usage from the collection."""
    session = Session()
    
    usage = session.query(Usage).get(id)
    if usage is not None:
        session.delete(usage)
        session.commit()
        click.echo(f"Removed usage with ID {id}.")
    else:
        click.echo(f"No usage found with ID {id}.")


@click.command()
def list_usages():
    """List all usages in the collection."""
    session = Session()
    
    usages = session.query(Usage).all()
    for usage in usages:
        click.echo(f"ID: {usage.id}")
        click.echo(f"Gemstone ID: {usage.gemstone_id}")
        click.echo(f"Practitioner ID: {usage.practitioner_id}")
        click.echo(f"Member ID: {usage.member_id}")
        click.echo(f"Start Date: {usage.start_date}")
        click.echo(f"End Date: {usage.end_date}")
        click.echo("-------")


commands = [add_usage, remove_usage, update_usage, list_usages]
