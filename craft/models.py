# vendor/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields can go here if needed
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to something unique
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change this to something unique
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='product_images/')
  
    def __str__(self):
        return self.name
