from django.db import models    #Going to make models 

# Create your models here.
class Book(models.Model): #for models
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)

    def __str__(self):      #converts object to human readable form 
        return self.title   #list out in the base of title 