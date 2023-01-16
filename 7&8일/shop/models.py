from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField()
    likey = models.IntegerField()

    def __str__(self):
        return self.name