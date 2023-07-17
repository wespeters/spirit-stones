from models import Gemstone, Practitioner, Member, Usage, Session
from datetime import datetime

def seed_database():
    session = Session()

    quartz = Gemstone(name='Quartz', color='Clear', properties='Amplification, clearing, cleansing', availability=True)
    amethyst = Gemstone(name='Amethyst', color='Purple', properties='Protection, purification, divine connection', availability=True)
    session.add_all([quartz, amethyst])

    alice = Practitioner(name='Alice', specialization='Crystal Healing')
    bob = Practitioner(name='Bob', specialization='Reiki')
    session.add_all([alice, bob])

    charlie = Member(name='Charlie')
    dana = Member(name='Dana')
    session.add_all([charlie, dana])

    usage1 = Usage(gemstone_id=quartz.id, practitioner_id=alice.id, member_id=charlie.id, start_date=datetime.now())
    usage2 = Usage(gemstone_id=amethyst.id, practitioner_id=bob.id, member_id=dana.id, start_date=datetime.now())
    session.add_all([usage1, usage2])

    session.commit()

if __name__ == '__main__':
    seed_database()
