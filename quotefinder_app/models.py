from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name  # Create your models here.


class Quote(models.Model):
    body = models.CharField(max_length=300)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='quotes', null=True)

    def __str__(self):
        return self.body
