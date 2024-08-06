from django.db import models
from flats.models import Flat
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class TenantProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None, flat=None, **extra_fields):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            flat=flat,
            username=None,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Tenant(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='tenants', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    username = None  # Disable the username field

    objects = TenantProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
