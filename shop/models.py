from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    sku = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False,default = 0)
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name + ':' + self.sku
