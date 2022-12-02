
from django.db import models

from users.models import Accounts

# Create your models here.


class Userprofile(models.Model):
    user = models.OneToOneField(Accounts, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name