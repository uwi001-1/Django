from django.db import models
# from django.utils import timezone
from author.models import Author
from genre.models import Genre
import uuid

# Create your models here.
class Book(models.Model):
    TYPE_CHOICES = (
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback')
    )
    title = models.CharField(max_length=255)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    book_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    isbn = models.CharField(max_length=13, unique=True)
    language = models.CharField(max_length=50)
    publication_year = models.PositiveIntegerField(blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title