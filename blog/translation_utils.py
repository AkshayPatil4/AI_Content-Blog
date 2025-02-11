import os
import subprocess
from django.conf import settings
from .models import TranslationEntry

def generate_po_file(language_code):
    """
    Generate a .po file from database translations for a specific language,
    including a full header.
    """
    locale_dir = os.path.join(settings.BASE_DIR, 'locale', language_code, 'LC_MESSAGES')
    os.makedirs(locale_dir, exist_ok=True)
    po_file_path = os.path.join(locale_dir, 'django.po')

    # Define the desired header (adjust dates and other fields as needed)
    header = '''# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2025-02-10 16:33+0100\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"Language: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=6; plural=n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 && n%100<=99 ? 4 : 5;\\n"

'''

    with open(po_file_path, 'w', encoding='utf-8') as po_file:
        # Write the header
        po_file.write(header)
        # Write each translation entry from the database for this language
        translations = TranslationEntry.objects.filter(language=language_code)
        for entry in translations:
            po_file.write(f'msgid "{entry.msgid}"\n')
            po_file.write(f'msgstr "{entry.msgstr}"\n\n')

    print(f"PO file generated: {po_file_path}")
    return po_file_path

def compile_po_to_mo(language_code):
    """Compile a .po file to a .mo file for a specific language."""
    locale_dir = os.path.join(settings.BASE_DIR, 'locale', language_code, 'LC_MESSAGES')
    po_file_path = os.path.join(locale_dir, 'django.po')
    mo_file_path = os.path.join(locale_dir, 'django.mo')

    if not os.path.exists(po_file_path):
        raise FileNotFoundError(f"PO file not found: {po_file_path}")

    # Call msgfmt to compile the .po file
    subprocess.run(['msgfmt', po_file_path, '-o', mo_file_path], check=True)
    print(f"MO file compiled: {mo_file_path}")
    
    