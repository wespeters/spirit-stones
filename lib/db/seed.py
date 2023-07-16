from models import Gemstone, Practitioner, Member, Usage, Session
from datetime import datetime

def seed_database():
    session = Session()

    # Create some gemstones
    quartz = Gemstone(name='Quartz', color='Clear', properties='Amplification, clearing, cleansing', availability=True)
    amethyst = Gemstone(name='Amethyst', color='Purple', properties='Protection, purification, divine connection', availability=True)
    session.add_all([quartz, amethyst])

    # Create some practitioners
    alice = Practitioner(name='Alice', specialization='Crystal Healing')
    bob = Practitioner(name='Bob', specialization='Reiki')
    session.add_all([alice, bob])

    # Create some members
    charlie = Member(name='Charlie')
    dana = Member(name='Dana')
    session.add_all([charlie, dana])

    # Create some usage records
    usage1 = Usage(gemstone_id=quartz.id, practitioner_id=alice.id, member_id=charlie.id, start_date=datetime.now())
    usage2 = Usage(gemstone_id=amethyst.id, practitioner_id=bob.id, member_id=dana.id, start_date=datetime.now())
    session.add_all([usage1, usage2])

    # Commit the session to write the data to the database
    session.commit()

if __name__ == '__main__':
    seed_database()
