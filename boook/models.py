from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=11, unique=True)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self):
        return self.title