from rest_framework import serializers
from .models import Post
from .models import TranslationEntry

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TranslationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationEntry
        fields = ['id', 'msgid', 'language', 'msgstr']