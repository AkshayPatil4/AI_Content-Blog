import json
from django import forms

class LanguageTranslationForm(forms.Form):
    language = forms.CharField(
        max_length=10,
        help_text="Enter the language code (e.g., 'hi' for Hindi)."
    )
    translations = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 120, 'rows': 40, 'placeholder': '''{
    "English": "अंग्रेज़ी",
    "Arabic": "अरबी",
    "AI Blog": "एआई ब्लॉग",
    "Welcome to AI Blog": "एआई ब्लॉग में आपका स्वागत है",
    "All rights reserved.": "सर्वाधिकार सुरक्षित",
    "Latest AI Articles": "नवीनतम एआई लेख",
    "The Future of AI": "एआई का भविष्य",
    "Artificial Intelligence is evolving rapidly and impacting various industries. From healthcare to finance, AI is transforming the way we work and live.": "कृत्रिम बुद्धिमत्ता तेजी से विकसित हो रही है और विभिन्न उद्योगों पर प्रभाव डाल रही है। स्वास्थ्य देखभाल से लेकर वित्त तक, एआई हमारे काम करने और जीने के तरीके को बदल रहा है.",
    "AI in Healthcare": "स्वास्थ्य देखभाल में एआई",
    "AI is being used to diagnose diseases, develop personalized treatments, and even assist in surgeries. The potential of AI in medicine is limitless.": "एआई का उपयोग रोगों का निदान करने, व्यक्तिगत उपचार विकसित करने, और यहां तक कि सर्जरी में सहायता करने के लिए किया जा रहा है। चिकित्सा में एआई की संभावनाएँ असीमित हैं.",
    "The Role of AI in Automation": "स्वचालन में एआई की भूमिका",
    "Automation powered by AI is revolutionizing industries by improving efficiency and reducing human effort in repetitive tasks.": "एआई द्वारा समर्थित स्वचालन उद्योगों में क्रांति ला रहा है, जिससे दक्षता बढ़ती है और दोहराए जाने वाले कार्यों में मानवीय प्रयास कम होता है."
}'''}),
        help_text="Enter a valid JSON object with msgid keys and msgstr values."
    )

    def clean_translations(self):
        data = self.cleaned_data['translations']
        try:
            parsed_data = json.loads(data)
        except json.JSONDecodeError:
            raise forms.ValidationError("Invalid JSON data. Please check your syntax.")
        if not isinstance(parsed_data, dict):
            raise forms.ValidationError("The JSON data must be an object (i.e., a dictionary).")
        return parsed_data
