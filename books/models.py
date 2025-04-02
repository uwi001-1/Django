from django.db import models
# from django.utils import timezone
from author.models import Author
from genre.models import Genre
import uuid
from django.utils.text import slugify 

# Create your models here.
class Book(models.Model):
    TYPE_CHOICES = (
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback')
    )
    title = models.CharField(max_length=255, help_text='Title of the book')

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)

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
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify.slugify(self.title) + '-' + str(self.public_id)
    #     super(Book,self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.title)}-{str(self.public_id)[1:5]}{str(self.public_id)[-1:-5]}'
        super().save(*args, **kwargs)