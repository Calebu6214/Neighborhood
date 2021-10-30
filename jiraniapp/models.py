from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

Priority=(
    ('Low Attention','Low Attention'),
    ('High Attention','High Attention'),
)

class neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()

class Profile(models.Model):
    profpic = models.ImageField(upload_to='profilep/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
