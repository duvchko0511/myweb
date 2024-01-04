# models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.utils.text import slugify
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('topics', args=[self.slug])

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    images = models.ImageField(upload_to='photos/products', null=True, blank=True) 
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # new social media fields
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('category_topics', args=[self.category.slug, self.slug])
    @receiver(post_save, sender='category.Product')
    def resize_product_image(sender, instance, **kwargs):
        if instance.images:
            image_path = instance.images.path
            image = Image.open(image_path)

            # Set your desired dimensions for the image
            new_size = (300, 200)
            image.thumbnail(new_size)

            image.save(image_path)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

class ImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='topics/products', max_length=255)

    def __str__(self):
        return self.product.product_name

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    rating = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.title
from django import forms
from .models import Product

