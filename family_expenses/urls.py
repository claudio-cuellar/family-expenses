from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path("expenses/", include("apps.expenses.urls")),
    path('reports/', include('apps.reports.urls')),
]

if settings.DEBUG:
    # Only serve static files, NOT media files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Remove this line to block direct media access:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)