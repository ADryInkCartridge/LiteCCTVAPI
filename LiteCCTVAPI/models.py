from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.TextField()
    imagedata = models.TextField()
    token = models.TextField()
    def __str__(self):
        return self.filename

class Token(models.Model):
    token = models.TextField(unique=True)
    def __str__(self):
        return self.token

class FaceImage(models.Model):
    image_data = models.TextField()
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_data
    
    

