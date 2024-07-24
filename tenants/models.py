from django.db import models
from flats.models import Flat
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class TenantProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Tenant(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='tenants')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = TenantProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
