from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=20)
    # def __str__(self):
    #     return self.name