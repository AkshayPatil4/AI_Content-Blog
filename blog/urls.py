from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import blog_list

router = DefaultRouter()
router.register(r'posts', PostViewSet)  

urlpatterns = [
    path('', blog_list, name='blog-list'),
]
