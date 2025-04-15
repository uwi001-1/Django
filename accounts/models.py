from django.db import models
import uuid
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=15, null=True, default='')
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    professional_image = models.ImageField(upload_to='profile', null=True, blank=True)
    position = models.PositiveIntegerField(default=0)

    # active_workspace = models.ForeignKey(
    #     "workspace.Workspace", on_delete=models.SET_NULL, null=True, blank=True, related_name="active_users"
    # )

    groups = models.ManyToManyField(Group, related_name='customer_groups', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    created_date = models.DateTimeField(auto_now_add=True)
    updates_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email