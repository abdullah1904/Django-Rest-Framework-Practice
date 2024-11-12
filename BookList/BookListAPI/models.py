from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    author = models.ForeignKey(Author, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.title