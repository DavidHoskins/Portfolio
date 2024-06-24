from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField("birthdate")

class Book(models.Model):
    name = models.CharField(max_length=50)
    publish_data = models.DateTimeField("date published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)