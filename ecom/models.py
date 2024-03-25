from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def category(self, category_name):
        return self.get_queryset().filter(category_name=category_name)

    def get_queryset(self):
        return super().get_queryset().filter(price__gt=200)

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField( max_length=50)
    price=models.IntegerField(null=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static')
    custom_objects = ProductManager()

    
    def __str__(self):
        return self.name    




