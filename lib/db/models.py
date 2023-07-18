from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine('sqlite:///spiritstones.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Gemstone(Base):
    __tablename__ = 'gemstones'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    properties = Column(String)
    availability = Column(Boolean, default=True)
    
    usages = relationship('Usage', back_populates='gemstone')

    def update_availability(self, session):
        # Check if there is a usage without an end date
        open_usage = session.query(Usage).filter(Usage.gemstone_id == self.id, Usage.end_date == None).first()

        # If there is such a usage, the gemstone is not available
        if open_usage:
            self.availability = False
        else:
            self.availability = True
            

class Practitioner(Base):
    __tablename__ = 'practitioners'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    
    usages = relationship('Usage', back_populates='practitioner')

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    usages = relationship('Usage', back_populates='member')

class Usage(Base):
    __tablename__ = 'usages'
    
    id = Column(Integer, primary_key=True)
    gemstone_id = Column(Integer, ForeignKey('gemstones.id'))
    practitioner_id = Column(Integer, ForeignKey('practitioners.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    gemstone = relationship('Gemstone', back_populates='usages')
    practitioner = relationship('Practitioner', back_populates='usages')
    member = relationship('Member', back_populates='usages')
