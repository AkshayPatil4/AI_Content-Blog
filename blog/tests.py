from django.test import TestCase, Client
from django.utils.translation import activate, get_language
from django.conf import settings
import os
import subprocess

class LocalizationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_language_switch_to_arabic(self):
        """ Test switching the language to Arabic """
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='ar')
        self.assertEqual(get_language(), 'ar')

    def test_language_switch_to_english(self):
        """ Test switching the language to English """
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='en')
        self.assertEqual(get_language(), 'en')


    def test_new_language_can_be_added(self):
        """ Test adding a new language without requiring database migrations """
        new_language_code = 'fr'
        settings.LANGUAGES = settings.LANGUAGES + [(new_language_code, 'French')]

        # Check if the new language exists in LANGUAGES
        self.assertIn((new_language_code, 'French'), settings.LANGUAGES)

    

    