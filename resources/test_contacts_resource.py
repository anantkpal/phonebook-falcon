import falcon
from falcon import testing
import json
from unittest import TestCase
from unittest.mock import patch

from app import api
from services import contact_service


class TestContactsModule(TestCase):

    def setUp(self):
        self.client = testing.TestClient(api)

    @patch.object(contact_service, 'find_all_contacts')
    def test_list_empty_contacts(self, find_all_contacts):
        find_all_contacts.return_value = []
        response = self.client.simulate_get('/contacts')
        result_doc = json.loads(response.content)

        assert result_doc == []
        assert response.status == falcon.HTTP_200

    @patch.object(contact_service, 'find_all_contacts')
    def test_list_contacts(self, find_all_contacts):
        find_all_contacts.return_value = [{
            'first_name': 'Anant',
            'last_name': 'Pal',
        }]
        response = self.client.simulate_get('/contacts')
        result_doc = json.loads(response.content)

        assert result_doc == [{
            'first_name': 'Anant',
            'last_name': 'Pal',
        }]
        assert response.status == falcon.HTTP_200

    @patch.object(contact_service, 'create_contact')
    def test_create_contacts(self, create_contact):
        create_contact.return_value = {
            'id': 1,
            'first_name': 'Anant',
            'last_name': 'Pal',
        }
        response = self.client.simulate_post(
            '/contacts',
            body=json.dumps({
                'first_name': 'Anant',
                'last_name': 'Pal',
            }),
            headers={'content-type': 'application/json'}
        )
        result_doc = json.loads(response.content)

        assert result_doc == {
            'id': 1,
            'first_name': 'Anant',
            'last_name': 'Pal',
        }
        assert response.status == falcon.HTTP_200
        create_contact.assert_called_with(first_name='Anant', last_name='Pal')

    @patch.object(contact_service, 'update_contact')
    def test_update_contact(self, update_contact):
        update_contact.return_value = {
            'id': 1,
            'first_name': 'Anant',
            'last_name': 'Pal',
        }
        response = self.client.simulate_patch(
            '/contacts/1',
            body=json.dumps({
                'first_name': 'Anant',
                'last_name': 'Pal',
            }),
            headers={'content-type': 'application/json'}
        )
        result_doc = json.loads(response.content)

        assert result_doc == {
            'id': 1,
            'first_name': 'Anant',
            'last_name': 'Pal',
        }
        assert response.status == falcon.HTTP_200
        update_contact.assert_called_with(1, {
            'first_name': 'Anant',
            'last_name': 'Pal',
        })

    @patch.object(contact_service, 'update_contact')
    def test_update_contact_with_invalid_id(self, update_contact):
        update_contact.return_value = None
        response = self.client.simulate_patch(
            '/contacts/1',
            body=json.dumps({
                'first_name': 'Anant',
                'last_name': 'Pal',
            }),
            headers={'content-type': 'application/json'}
        )

        assert response.status == falcon.HTTP_404
        update_contact.assert_called_with(1, {
            'first_name': 'Anant',
            'last_name': 'Pal',
        })

    @patch.object(contact_service, 'get_contact')
    def test_get_contact(self, get_contact):
        get_contact.return_value = {
            'id': 1,
            'first_name': 'Anant',
            'last_name': 'Pal',
        }
        response = self.client.simulate_get('/contacts/1')
        result_doc = json.loads(response.content)

        assert result_doc == {
            'id': 1,
            'first_name': 'Anant',
            'last_name': 'Pal',
        }
        assert response.status == falcon.HTTP_200
        get_contact.assert_called_with(1)

    @patch.object(contact_service, 'get_contact')
    def test_get_contact_with_invalidid(self, get_contact):
        get_contact.return_value = None
        response = self.client.simulate_get('/contacts/1')
        assert response.status == falcon.HTTP_404
        get_contact.assert_called_with(1)

    @patch.object(contact_service, 'delete_contact')
    def test_successfully_delete_contact(self, delete_contact):
        delete_contact.return_value = True
        response = self.client.simulate_delete('/contacts/1')
        assert response.status == falcon.HTTP_200
        delete_contact.assert_called_with(1)

    @patch.object(contact_service, 'delete_contact')
    def test_failed_delete_contact(self, delete_contact):
        delete_contact.return_value = False
        response = self.client.simulate_delete('/contacts/1')
        assert response.status == falcon.HTTP_404
        delete_contact.assert_called_with(1)
