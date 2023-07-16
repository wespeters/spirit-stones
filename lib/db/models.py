from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
