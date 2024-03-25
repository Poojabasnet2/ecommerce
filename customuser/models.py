from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.db import models
USER_ROLES=(('user','user'),
('vendor','vendor'))
class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )
        return user





# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=25,blank=True)
    role=models.CharField(choices=USER_ROLES,max_length=50)

