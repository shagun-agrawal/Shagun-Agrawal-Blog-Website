from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=70)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    birthdate=models.DateField(null=True)

    def __str__(self):
        return self.username
class Data(models.Model):
    title_name=models.CharField(max_length=70)
    title=models.TextField()
    photo = models.ImageField(upload_to="myimage/")

    def __str__(self):
        return self.title_name