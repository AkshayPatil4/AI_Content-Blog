from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import blog_list, PostViewSet, TranslationViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'translations', TranslationViewSet)

urlpatterns = [
    path('', blog_list, name='home'),
    path('api/', include(router.urls)),
]
