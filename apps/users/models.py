from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class FamilyRole(models.TextChoices):
        PARENT = 'parent', 'Parent'
        CHILD = 'child', 'Child'
        GUEST = 'guest', 'Guest'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    family_role = models.CharField(
        max_length=10,
        choices=FamilyRole.choices,
        default=FamilyRole.GUEST,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email