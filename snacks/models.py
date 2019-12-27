from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Product(models.Model):
    """Class Models for Products"""
    ean = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(
        default='product_default.png', upload_to='products_pics')
    nutriscore = models.CharField(max_length=1)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return self.name

    def get_absolute_url(self):
        """Provides absolute URL for product detail page"""
        return reverse('detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        """Overwrite the save() method with custom informations"""
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Favourite(models.Model):
    """Class Models for Favourite"""
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User: {self.user}, Favourite: {self.product}, \
Date: {self.date_added}"

    def get_absolute_url(self):
        """calling the object detailed page's absolute url"""
        return reverse('detail', kwargs={'pk': self.pk})
