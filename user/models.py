from django.db import models
from datetime import date
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, organization, title, phone_number):

        # Normalize data
        first_name = first_name.lower()
        last_name = last_name.lower()
        email = email.lower()

        # Not necessary
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model (
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            email=self.normalize_email(email),
            organization=organization,
            title=title,
            phone_number=phone_number
        )

        # Set hashed password and save user
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, first_name, last_name, password, organization, title, phone_number):

        # Normalize data
        first_name = first_name.lower()
        last_name = last_name.lower()
        email = email.lower()

        user = self.create_user (
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            organization=organization,
            title=title,
            phone_number=phone_number
        )

        # Set defaults and save user
        # Test to make sure the password is still being hashed for superusers..
        # May need to add 'user.set_password(password)'
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    CHOICES_ORG = (
        ('City_A', 'City A'),
        ('City_B', 'City B'),
        ('City_C', 'City C'),
        ('Tulsa', 'Tulsa'),
        ('Fort_Wayne', 'Fort Wayne'),
        ('Stillwater', 'Stillwater'),
        ('Laredo', 'Laredo'),
        ('Baltimore', 'Baltimore'),
        ('New_City', 'New City'),
        ('Glenpool', 'Glenpool'),
        )
    CHOICES_TITLE = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        )
    
    first_name         = models.CharField(max_length=150, blank=True)
    last_name          = models.CharField(max_length=150, blank=True)
    email              = models.EmailField(max_length=150, verbose_name="email address", unique=True)
    organization       = models.CharField(verbose_name="organization", max_length=150, choices = CHOICES_ORG, blank=True)
    title              = models.CharField(verbose_name="title", max_length=150, choices = CHOICES_TITLE, blank=True)
    phone_number       = models.CharField(verbose_name="phone number", max_length=15, blank=True)
    is_staff           = models.BooleanField(default=False)
    is_organizational_staff = models.BooleanField(default=False)
    is_active          = models.BooleanField(default=True)
    start_date         = models.DateTimeField(auto_now_add=True, blank=True)
    isToggled          = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'organization', 'title', 'phone_number']

    def __str__(self):
        return self.email
    
    def getFullName(self):
        return self.first_name + " " + self.last_name
    
    # Need to research perms more
    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_staff
    """
    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    """


