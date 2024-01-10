# models.py
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-generate the slug when saving the product
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    # other fields and methods in your model


# models.py
class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5, null=True)


    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.postal_code}"

