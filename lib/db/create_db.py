# create_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # assuming models.py is in the same directory

engine = create_engine('sqlite:///spiritstones.db')
Session = sessionmaker(bind=engine)

# Create all tables in the engine.
# "Base" contains the metadata where SQLAlchemy has been keeping track of all your models.
Base.metadata.create_all(engine)
