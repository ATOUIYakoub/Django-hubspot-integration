from django.test import TestCase, Client
from django.urls import reverse
import json
from unittest.mock import patch

class HubSpotIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.update_url = reverse('update_hubspot_lead', kwargs={'pk': '36659094211'})
        self.valid_payload = {
            "properties": {
                "firstname": "new_firstname",
                "lastname": "new_lastname"
            }
        }

    @patch('analytics.views.update_hubspot_lead')
    def test_update_hubspot_lead(self, mock_update_hubspot_lead):
        mock_update_hubspot_lead.return_value.status_code = 200
        mock_update_hubspot_lead.return_value.json.return_value = {
            "properties": {
                "firstname": "new_firstname",
                "lastname": "new_lastname"
            }
        }

        response = self.client.put(
            self.update_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('new_firstname', response.json()['results'][0]['firstname'])
        self.assertIn('new_lastname', response.json()['results'][0]['lastname'])