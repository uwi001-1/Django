from django.db import models
from author.models import Author
from genre.models import Genre
from reviews.models import Reviews
from stock.models import Stock

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Reviews, related_name='reviews', blank=True, null=True)
    stock = models.OneToOneField(Stock)
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
    