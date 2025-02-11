from django.urls import path, re_path, include
from django.views.i18n import set_language
from django.contrib import admin
from django.shortcuts import redirect
from blog.admin import admin_site

urlpatterns = [
    # Redirect the empty path to the default language (e.g., English)
    path('', lambda request: redirect('/en/', permanent=False)),
    
    # Use a dynamic pattern that accepts any two-letter language code
    re_path(r'^(?P<language>[a-z]{2})/', include('blog.urls')),
    
    # URL for the set-language view
    path('set-language/', set_language, name='set_language'),
    
    path('admin/', admin_site.urls),
]
