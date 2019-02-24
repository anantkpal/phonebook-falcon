from unittest import TestCase
from unittest.mock import patch, MagicMock

from models.contact import Contact
from services import contact_service, base_repo


class TestContactService(TestCase):

    @patch.object(base_repo, 'get_details')
    def test_get_contact(self, mock_get):
        contact_mock = MagicMock()
        mock_get.return_value = contact_mock

        contact = contact_service.get_contact(1)
        assert contact == contact_mock.to_dict()

        mock_get.assert_called_with(Contact, 1)

    @patch.object(base_repo, 'get_details')
    def test_get_contact_invalid_id(self, mock_get):
        mock_get.return_value = None

        contact = contact_service.get_contact(1)
        mock_get.assert_called_with(Contact, 1)
        assert contact == None

    @patch.object(base_repo, 'delete')
    def test_delete_contact(self, mock_delete):
        contact_service.delete_contact(1)
        mock_delete.assert_called_with(Contact, 1)

    @patch.object(base_repo, 'create')
    def test_create_contact(self, mock_create):
        contact_service.create_contact(first_name='Anant', last_name='Pal', phone='987654321',
                                       email='sample@exampl.com')
        mock_create.assert_called_once()

    @patch.object(base_repo, 'find_all')
    def test_get_contacts(self, mock_find_all):
        contacts = [MagicMock()]
        mock_find_all.return_value = contacts
        results = contact_service.find_all_contacts()
        mock_find_all.assert_called_with(Contact)

        assert results == [contact.to_dict() for contact in contacts]

    @patch.object(base_repo, 'update')
    @patch.object(base_repo, 'get_details')
    def test_update_contact(self, mock_get_details, mock_update_contact):
        contact = MagicMock()
        mock_get_details.return_value = contact
        result = contact_service.update_contact(1, {'first_name': 'Anant'})
        mock_get_details.assert_called_with(Contact, 1)
        mock_update_contact.assert_called_with(Contact, 1, {'first_name': 'Anant'})

        assert result == contact.to_dict()
