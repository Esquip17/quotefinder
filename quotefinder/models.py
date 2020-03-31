from django.db import models


class Quote(models.Model):
    body = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
