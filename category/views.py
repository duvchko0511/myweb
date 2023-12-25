# Create your views here.
from sqlite3 import Connection
from django.http import Http404
from django.shortcuts import render , get_object_or_404, redirect
from psycopg2 import connect
from cart_app.models import CartItem
from cart_app.views import _cart_id
from .models import Category, Product, ImageGallery, ReviewRating
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Avg
def topics_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True).order_by('-id')[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'uilajillagaa/topics.html', context)
# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True).order_by('-id')[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, "index.html", context)

def product_detail(request, category_slug, product_slug):
    try:
        # Retrieve the product using slugs
      product = Product.objects.get(category__slug=category_slug, slug=product_slug)
      product_gallery = ImageGallery.objects.filter(product_id=product.id)
    except Exception as e:
        raise e 
    context = {
        'single_products':product_gallery,
        'product_gallery':product_gallery
    }
    return render(request, 'uilajillagaa/product-detail.html', context)

def search_result(request):
    return render(request, "search-result.html")
def topics(request, category_slug = None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category = categories)
        count=products.count()
        p=Paginator(products, 1)
        page = request.GET.get("page")
        paged_products = p.get_page(page)
    elif category_slug is None:
        products = Product.objects.filter(is_available = True)
        count=products.count()
        p=Paginator(products, 1)
        page = request.GET.get("page")
        paged_products = p.get_page(page)
    else:
        categories = Category.objects.all()
        products = Product.objects.filter(category = categories)
        count=products.count()
        p=Paginator(products, 2)
        page = request.GET.get("page")
        paged_products = p.get_page(page)
    context = {
        'products': paged_products,
        'categories': categories,
        'count': count
    }
    return render(request, "uilajillagaa/topics.html", context) 
def home(request):
    categories = Category.objects.all()

    # Establish a connection to the PostgreSQL database

    # Create a cursor to execute SQL queries
    cur = connect.cursor()

    # Execute a sample SQL query (replace it with your actual query)
    cur.execute("SELECT * FROM your_table_name")
    rows = cur.fetchall()
    print(rows)
    size = len(rows)

    # Fetch all products that are available
    products = Product.objects.filter(is_available=True)

    # Close the cursor and connection
    cur.close()
    Connection.close()

    context = {
        'categories': categories,
        'products': products,
        'size': size,
    }

    return render(request, "home.html", context)
def search(request):
    keyword = request.GET.get('keyword', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    product_query = Q(product_name__icontains=keyword) | Q(description__icontains=keyword)

    if min_price is not None and max_price is not None:
        products = Product.objects.filter(product_query, price__range=(min_price, max_price))
    elif min_price is not None:
        products = Product.objects.filter(product_query, price__gte=min_price)
    elif max_price is not None:
        products = Product.objects.filter(product_query, price__lte=max_price)
    else:
        products = Product.objects.filter(product_query)

    count = products.count()

    context = {
        'products': products,
        'count': count,
        'keyword': keyword,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'uilajillagaa/topics.html', context) 
def submit_review(request, product_id):
    if request.method == 'POST':
        rev = ReviewRating()
        rev.product = product_id
        rev.user = request.user.id
        rev.title = request.POST['title']
        rev.review = request.POST['review']
        rev.rating = request.POST['rate']
        rev.ip = request.META.get('REMOTE_ADDR')
        rev.save()
        pr = Product.objects.get(id=product_id)
        return redirect(pr.get_url())