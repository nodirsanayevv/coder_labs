from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
