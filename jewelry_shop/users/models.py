
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


from django.core.validators import RegexValidator 
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Accounts(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'^(?:\+88|88)?(01[3-9]\d{8})$', message="Phone number must be entered in the format: '+8801XXXXXX'. Up to 14 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=20, unique=True,null=True,blank=True)


    is_verified = models.BooleanField(
        ('verified'),
        default=False, 
        help_text=(
            'Designates whether this user has been verified.'
            'Un-verified users cannot log in.'
        ),
    )

    is_saler = models.BooleanField(
        ('Saler Permission'),
        default=False,
        help_text=(
            'Designates whether this user should be treated as founder.'
        ),
    )


    created_at = models.DateTimeField(default=now, editable=False)
    
    profile_pic = models.FileField(upload_to='profile_pic',null=True,blank=True)
    address = models.TextField(null=True,blank=True)



    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()


    def __str__(self):
        return self.email



