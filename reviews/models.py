from django.db import models
from books.models import Book

# Create your models here.
class Reviews(models.Model):
    name = models.CharField(max_length=255)
    ratings = models.PositiveIntegerField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name