from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_user'
    username = models.CharField(max_length=20, default="ๅ็กใ",unique=True, )
    phone = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.username)