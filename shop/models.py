from django.db import models

# Create your models here.

class GenericCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class GenericValues(models.Model):
    category = models.ForeignKey(GenericCategory, on_delete=models.CASCADE, related_name="generic_category") 
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")

    def __str__(self):
        return self.name
    
class ProductFilter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(GenericCategory, on_delete=models.CASCADE)
    value = models.ForeignKey(GenericValues, on_delete=models.CASCADE)