from django.apps import AppConfig
from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        from blog.models import TranslationEntry  # Import here to avoid early import issues
        try:
            language_codes = TranslationEntry.objects.values_list("language", flat=True).distinct()
            # Convert settings.LANGUAGES into a dict for easy lookup.
            current_langs = dict(settings.LANGUAGES)
            for code in language_codes:
                if code not in current_langs:
                    settings.LANGUAGES.append((code, code.capitalize()))
        except (OperationalError, ProgrammingError):
            # In case the database isn’t ready or migrated, just pass.
            pass
