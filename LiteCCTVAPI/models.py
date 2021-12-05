from django.db import models

# Create your models here.
class Image(models.Model):
    filename = models.TextField()
    imagedata = models.TextField()
    token = models.TextField()
    def __str__(self):
        return self.filename

class Token(models.Model):
    token = models.TextField(unique=True)
    def __str__(self):
        return self.token

