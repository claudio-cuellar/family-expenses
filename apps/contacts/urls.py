from django.urls import path
from .views import ContactCreateView, ContactListView

urlpatterns = [
    path('create/', ContactCreateView.as_view(), name='contact_create'),
    path('list/', ContactListView.as_view(), name='contact_list'),
]