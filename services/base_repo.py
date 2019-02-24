from models.base import Session

session = Session()


def create(instance):
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def find_all(model):
    return session.query(model).all()


def get_details(model, id):
    return session.query(model).filter(model.id == id).first()


def update(model, id, update_args):
    session.query(model).filter(model.id == id).update(update_args)

def delete(model, id):
    instance = get_details(model, id)
    if instance:
        session.query(model).filter(model.id == id).delete()
        return True
    return False
