from faker import Faker
import random
from models import Audition, Role, sessionmaker, create_engine, Base

fake = Faker()

engine = create_engine('sqlite:///auditions.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_audition():
    auditions = [
        Audition(
        actor=fake.name(),
        location=fake.address(),
        phone=str(fake.phone_number()),
        )
        for i in range(100)
    ]
    session.add_all(auditions)
    session.commit()
    return auditions

def create_role():
    roles = [
        Role(
        character_name=fake.name()
        )
        for i in range(100)
    ]
    session.add_all(roles)
    session.commit()
    return roles

def create_one_to_many(roles, auditions):
    for audition in auditions:
        audition.role = random.choice(roles)

    session.add_all(auditions)
    session.commit()
    return roles, auditions

def delete_db():
    session.query(Role).delete()
    session.query(Audition).delete()
    session.commit()

if __name__ == '__main__':
    session.close()
    delete_db()
    auditions = create_audition()
    roles = create_role()
    create_one_to_many(roles, auditions)


