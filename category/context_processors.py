


from .models import *
from django.db.models import Q, Avg
def menu_links(request):
    links = Category.objects.all()
    return {'links':links}
def rating(request):
    product_id = request.GET.get('product_id')

    try:
        if product_id:
            product_ratings = ReviewRating.objects.filter(product_id=product_id)
            average_rating = product_ratings.aggregate(Avg('rating'))['rating__avg']
        else:
            average_rating = None
    except ReviewRating.DoesNotExist:
        average_rating = None

    return {'average_rating': average_rating}