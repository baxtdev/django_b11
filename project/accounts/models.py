from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# from .managers import CustomUserManager


class CustomUser(AbstractUser):
    phone = models.CharField(
        'Телефон',
        max_length=15,
        blank=True,
        null=True
    )    
    is_married = models.BooleanField(
        'is married',
        default=False
    )
    age = models.PositiveSmallIntegerField(
        'Возраст',
        blank=True,
        null=True
    )
    

    
