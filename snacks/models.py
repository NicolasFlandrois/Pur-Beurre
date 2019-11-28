from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Product(models.Model):
    """docstring for Products"""
    ean = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(
        default='products_default.jpg', upload_to='products_pics')
    nutriscore = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Favourite(models.Model):
    """docstring for Favourite"""
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return {"User": self.user, "Favourite": self.product,
                "Date": self.date_added}

    def get_absolute_url(self):
        return reverse('favourite-detail', kwargs={'pk': self.pk})
