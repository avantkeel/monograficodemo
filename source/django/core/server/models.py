# ⚠️ Deprecated module
# This code is no longer maintained.
# Do not use for new features.

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    passwordhash = models.CharField(max_length=255)

    def __str__(self):
        return self.username
