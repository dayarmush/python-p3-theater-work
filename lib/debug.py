from models import Audition, Role
from seed import session

if __name__ == '__main__':
    roles = session.query(Role).limit(5).all()

    r1 = session.query(Role).first()
    r2 = roles[3]
    a1 = session.query(Audition).first()

    import ipdb; ipdb.set_trace()