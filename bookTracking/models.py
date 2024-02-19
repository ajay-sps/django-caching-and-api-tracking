from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 40)
    price = models.IntegerField()
    author = models.ForeignKey(Author,on_delete = models.PROTECT)

    def __str__(self):
        return self.title