from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default=False)
    role_id = Column(Integer(), ForeignKey('roles.id'))

    def call_back(self):
        self.hired = True
        return self

    def __repr__(self):
        return f'Audition(Actor: {self.actor}, Hired: {self.hired})'
    
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key = True)
    character_name = Column(String())

    auditions = relationship('Audition', backref='role')

    def get_actors(self):
        actors = []
        for audition in self.auditions:
            actors.append(audition.actor)
        return actors
    
    def get_locations(self):
        locations = []
        for audition in self.auditions:
            locations.append(audition.location)
        return locations
    
    def lead(self):
        for audition in self.auditions:
            if audition.hired:
                return audition
            else:
                return 'no actor has been hired for this role'
            
    def under_study(self):
        hires = []
        for audition in self.auditions:
            if audition.hired:
                hires.append(audition)
        return hires[1] if hires else 'no actor has been hired for understudy for this role' 

    def __repr__(self):
        return f'Role(Character name: {self.character_name})'