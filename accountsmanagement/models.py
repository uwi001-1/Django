from django.db import models

# Create your models here.
class AccountsManagement(models.Model):
    name = models.CharField(max_length=250)