from django import forms
from django.utils.text import slugify
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'description', 'category', 'images', 'facebook_url', 'twitter_url',]

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)

        # Generate a unique slug based on the product name if it is not provided
        if not instance.slug:
            slug = slugify(instance.product_name)
            instance.slug = slug

        if commit:
            instance.save()

        return instance