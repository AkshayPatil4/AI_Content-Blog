from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TranslationEntry(models.Model):
    msgid = models.CharField(
        max_length=255,
        help_text="Original text (English)"
    )
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        help_text="Language code"
    )
    msgstr = models.TextField(help_text="Translated text")

    def __str__(self):
        return f"{self.language}: {self.msgid} -> {self.msgstr}"

class Meta:
    unique_together = ('msgid', 'language')  # Ensure unique translations per language
    
class LanguageTranslationTool(models.Model):
    """
    Dummy model used to provide a link in the admin to add language translations.
    """
    class Meta:
        managed = False  # No database table will be created.
        verbose_name = "Add Language Translation"
        verbose_name_plural = "Add Language Translation"
        app_label = "Translation Tools"    

    