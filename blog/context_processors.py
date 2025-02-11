from blog.models import TranslationEntry
from django.conf import settings

def available_languages(request):
    """
    Returns only the languages (from settings.LANGUAGES) that have at least one
    translation entry in the database, with English always included as the default.
    """
    # Get all language codes that have at least one translation entry
    langs_in_db = set(TranslationEntry.objects.values_list('language', flat=True))
    
    # Filter settings.LANGUAGES to only include those languages that are in the database
    available = [(code, name) for code, name in settings.LANGUAGES if code in langs_in_db]
    
    # Always ensure that English ('en') is present
    if not any(code == 'en' for code, name in available):
        # Look for 'en' in settings.LANGUAGES; if not found, use a default tuple.
        for code, name in settings.LANGUAGES:
            if code == 'en':
                available.append((code, name))
                break
        else:
            available.append(('en', 'English'))
    
    return {'LANGUAGES': available}
