
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from .models import TranslationEntry, Post
from .serializers import TranslationEntrySerializer, PostSerializer
from .translation_utils import generate_po_file, compile_po_to_mo
import logging
from django.utils.translation import trans_real

logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def blog_list(request, language=None):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

class TranslationViewSet(viewsets.ModelViewSet):
    queryset = TranslationEntry.objects.all()
    serializer_class = TranslationEntrySerializer

    def create(self, request, *args, **kwargs):
        language_code = request.data.get("language")
        translations = request.data.get("translations", {})

        if not language_code or not translations:
            return Response(
                {"error": "Language and translations required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        saved_entries = []
        for msgid, msgstr in translations.items():
            entry, created = TranslationEntry.objects.update_or_create(
                language=language_code,
                msgid=msgid,
                defaults={"msgstr": msgstr}
            )
            saved_entries.append(entry)

        # Update settings.LANGUAGES dynamically if not already present
        available_langs = dict(settings.LANGUAGES)
        if language_code not in available_langs:
            settings.LANGUAGES.append((language_code, language_code.capitalize()))
            logger.info(f"Language '{language_code}' added to settings.LANGUAGES.")

        # Generate and compile translation files.
        po_file_path = generate_po_file(language_code)
        try:
            compile_po_to_mo(language_code)
            # Reload the language to clear Django's translation cache
            from .views import reload_translation  # Ensure this is imported correctly
            reload_translation(language_code)
        except Exception as e:
            return Response(
                {"error": f"Translations saved, but error compiling MO file: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {
                "message": f"Translations saved for {language_code}",
                "saved_entries": [f"{entry.msgid} -> {entry.msgstr}" for entry in saved_entries]
            },
            status=status.HTTP_201_CREATED
        )
        
        
def reload_translation(language_code):
    # Remove the cached translation for the language.
    trans_real._translations.pop(language_code, None)
    # Optionally, force a reload by calling translation(language_code)
    trans_real.translation(language_code)