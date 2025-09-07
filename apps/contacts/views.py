from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny,)