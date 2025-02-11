from django.test import TestCase, Client
from django.utils.translation import activate, get_language
from django.conf import settings
import json
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class LocalizationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_language_switch_to_arabic(self):
        """Test switching the language to Arabic."""
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='ar')
        self.assertEqual(get_language(), 'ar')

    def test_language_switch_to_english(self):
        """Test switching the language to English."""
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='en')
        self.assertEqual(get_language(), 'en')

    def test_new_language_can_be_added(self):
        """Test that a new language can be added to settings.LANGUAGES without schema changes."""
        new_language_code = 'fr'
        settings.LANGUAGES = settings.LANGUAGES + [(new_language_code, 'French')]
        self.assertIn((new_language_code, 'French'), settings.LANGUAGES)


class TranslationAPITests(TestCase):
    def setUp(self):
        # Use DRF's APIClient for REST API tests.
        self.client = APIClient()
        # Create and authenticate a test superuser.
        self.user = User.objects.create_superuser('admin', 'admin@example.com', 'password123')
        self.client.force_authenticate(user=self.user)
        # Use a language prefix in the URL.
        # For example, if testing French translations, the endpoint should be /fr/api/translations/
        self.url = '/fr/api/translations/'

    def test_create_translation_api(self):
        """Test creating new translations via the REST API."""
        data = {
            "language": "fr",
            "translations": {
                "English": "Anglais",
                "Arabic": "Arabe",
                "AI Blog": "Blog d'IA",
                "Welcome to AI Blog": "Bienvenue sur le blog d'IA"
            }
        }
        response = self.client.post(self.url, data, format='json')
        # Expecting 201 Created.
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.data)
        self.assertIn("saved_entries", response.data)
        # Expecting 4 translation entries.
        self.assertEqual(len(response.data["saved_entries"]), 4)

    def test_update_translation_api(self):
        """Test updating existing translations via the REST API."""
        # Create initial translations.
        data = {
            "language": "fr",
            "translations": {
                "English": "Anglais",
                "Arabic": "Arabe"
            }
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        # Update the translations.
        data_update = {
            "language": "fr",
            "translations": {
                "English": "Anglais Updated",
                "Arabic": "Arabe Updated"
            }
        }
        response_update = self.client.post(self.url, data_update, format='json')
        self.assertEqual(response_update.status_code, 201)
        # Verify that updated translations are in the saved entries.
        saved_entries = response_update.data["saved_entries"]
        self.assertTrue(any("Anglais Updated" in entry for entry in saved_entries))
        self.assertTrue(any("Arabe Updated" in entry for entry in saved_entries))

    def test_retrieve_translations_api(self):
        """Test retrieving translations via the REST API."""
        # Create some translations.
        data = {
            "language": "fr",
            "translations": {
                "English": "Anglais",
                "Arabic": "Arabe"
            }
        }
        self.client.post(self.url, data, format='json')
        # Retrieve the list of translations.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # The response should be a list.
        self.assertTrue(isinstance(response.data, list))
        # At least one translation entry should be present.
        self.assertGreaterEqual(len(response.data), 1)
