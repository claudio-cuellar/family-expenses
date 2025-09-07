from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/', include('apps.users.urls')),
    path('contacts/', include('apps.contacts.urls')),
]