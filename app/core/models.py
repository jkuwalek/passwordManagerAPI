"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Website(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    websiteName = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    encryptedPassword = models.CharField(max_length=999)
    encryptedSalt = models.CharField(max_length=999)
    passwordStrength = models.FloatField()
    isLeaked = models.BooleanField(default=False)
    isUserCreated = models.BooleanField(default=True)
    userNotes = models.TextField(max_length=9999, blank=True)

    def __str__(self):
        return f"data-storage-id-{self.id} ({self.userId})"
