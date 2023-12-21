
# Register your models here.
from django.contrib import admin
from .models import Category, Product, ImageGallery, ReviewRating
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)
class ImageGalleryTabular(admin.TabularInline):
    model = ImageGallery
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ImageGalleryTabular]
admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating)

