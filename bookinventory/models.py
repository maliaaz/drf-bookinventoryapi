from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200, default='Book Title')
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=200)
    publication_date = models.DateField()

    def __str__(self):
        return self.name
