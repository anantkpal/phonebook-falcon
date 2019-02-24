from models.contact import Contact
from . import base_repo


def create_contact(**kwargs):
    contact = base_repo.create(Contact(**kwargs))
    return contact.to_dict()


def find_all_contacts():
    contacts = base_repo.find_all(Contact)
    return [contact.to_dict() for contact in contacts]


def get_contact(id):
    contact = base_repo.get_details(Contact, id)
    return contact.to_dict() if contact else None


def update_contact(id, update_details):
    base_repo.update(Contact, id, update_details)
    return get_contact(id)


def delete_contact(id):
    return base_repo.delete(Contact, id)
