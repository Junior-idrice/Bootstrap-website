from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=120)
    age = models.IntegerField(default=0)
    sex = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Product(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    postdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"