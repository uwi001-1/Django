from django.db import models
from books.models import Book

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    book = models.ManyToManyField(Book, related_name='author', blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_name