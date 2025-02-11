import os
import json
from django.urls import path
from django.contrib import admin, messages
from django.shortcuts import render, redirect
from .forms import LanguageTranslationForm
from .models import TranslationEntry
from .translation_utils import generate_po_file, compile_po_to_mo
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .models import LanguageTranslationTool

# Helper function to reload the translation cache
from django.utils.translation import trans_real, activate

def reload_translation(language_code):
    # Remove the cached translation for the language, then force a reload.
    trans_real._translations.pop(language_code, None)
    activate(language_code)

# Our custom admin view to add new language translations.
def add_language_translation_view(request):
    if request.method == 'POST':
        form = LanguageTranslationForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            translations = form.cleaned_data['translations']  # This should now be a dict
            # Log the type for debugging:
            # import logging; logging.info(f"Type of translations: {type(translations)}")
            
            # Iterate over the dictionary and create individual translation entries
            for msgid, msgstr in translations.items():
                TranslationEntry.objects.update_or_create(
                    language=language,
                    msgid=msgid,
                    defaults={'msgstr': msgstr}
                )
            
            # (Optional) Update settings.LANGUAGES if needed.
            from django.conf import settings
            available_langs = dict(settings.LANGUAGES)
            if language not in available_langs:
                settings.LANGUAGES.append((language, language.capitalize()))
            
            # Generate and compile translation files.
            generate_po_file(language)
            try:
                compile_po_to_mo(language)
                reload_translation(language)
            except Exception as e:
                messages.error(request, f"Translations saved, but error compiling MO file: {e}")
                return redirect("admin:add_language_translation")
            
            messages.success(request, f"Translations for language '{language}' have been saved and compiled.")
            return redirect("admin:add_language_translation")
    else:
        form = LanguageTranslationForm()
    
    context = {
        'form': form,
        'title': "Add New Language Translation"
    }
    return render(request, 'admin/add_language_translation.html', context)

# Create a custom AdminSite subclass to include our extra URL.
class MyAdminSite(admin.AdminSite):
    site_header = "My Admin"
    index_template = "admin/my_index.html"
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add-language-translation/', self.admin_view(add_language_translation_view), name='add_language_translation'),
        ]
        return custom_urls + urls

# Instantiate our custom admin site.
admin_site = MyAdminSite(name='myadmin')

# Register your models with the custom admin site (example):
from .models import Post, TranslationEntry
admin_site.register(Post)
admin_site.register(TranslationEntry)

class LanguageTranslationToolAdmin(admin.ModelAdmin):
    # Optionally, you can override the changelist template, but here we simply override the URLs.
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_site.admin_view(self.redirect_to_translation_view), name='language_translation_tool'),
        ]
        # Return the custom URL(s) before the default URLs.
        return custom_urls + urls

    def redirect_to_translation_view(self, request):
        # Redirect to your custom admin view URL.
        return redirect("admin:add_language_translation")  # URL name as defined in your custom admin site

# Register the dummy model with the custom ModelAdmin.
admin.site.register(LanguageTranslationTool, LanguageTranslationToolAdmin)