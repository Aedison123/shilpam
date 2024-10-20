# models.py

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    slogan = models.TextField(max_length=50)
    image = models.ImageField(upload_to='products/')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)  # Add this line
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

