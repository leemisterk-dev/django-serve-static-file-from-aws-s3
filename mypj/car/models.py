from django.db import models

# Create your models here.


class Car(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    sound=models.FileField(upload_to='sounds')

    def __str__(self):
        return self.name