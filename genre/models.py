from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre_name