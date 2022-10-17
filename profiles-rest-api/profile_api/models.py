from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, email, name, password=None):
        """
        Create a new user profile

        Because of the way the Django system works a None password
        will throw an error because passwords need to be a hash
        so not setting a password will not allow a user to authenticate
        """

        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # set_password function encrypts passwords in Django
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create new superuser with the specified details
        """

        # no need to pass self into a class function when you call it
        # it will be automatically passed in, this is part of python
        user = self.create_user(email,name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    # because we are defining a function within a class
    # we must pass in self as an argument
    # this is the default python convention
    def get_full_name(self):
        """
        Retrieve full name of user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name of user
        """
        return self.name

    def __str__(self):
        """
        Return data from our user cast as a string
        """
        return self.email

