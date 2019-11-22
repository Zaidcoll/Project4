from django.db import models

# Create your models here.

class CartItem(models.Model):
    
    product= models.ForeignKey('shop.Product',on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.MyUser',on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False,default = 0)
    
    def __str__(self):
        return self.product.name + ' x ' + str(self.quantity)