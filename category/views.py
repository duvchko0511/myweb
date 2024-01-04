# Create your views here.
from itertools import count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from sqlite3 import Connection
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render , get_object_or_404, redirect
from psycopg2 import connect
from cart_app.models import CartItem
from cart_app.views import _cart_id
from .models import Category, Product, ImageGallery, ReviewRating
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Avg
from .models import Product
from .forms import ProductForm
import logging
def topics_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True).order_by('-id')[:8]
    context = {
        'categories': categories,
        'products': products,
        'count':count
    }
    return render(request, 'uilajillagaa/topics.html', context)
# Create your views here.

from django.http import HttpResponseNotFound

logger = logging.getLogger(__name__)

def product_detail(request, category_slug, product_slug):
    try:
        # Retrieve the product using slugs
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        product_gallery = ImageGallery.objects.filter(product_id=product.id)
        
        # Get the product count for the category
        category_product_count = Product.objects.filter(category__slug=category_slug).count()

        context = {
            'single_products': product_gallery,
            'product_gallery': product_gallery,
            'category_product_count': category_product_count,
        }
        
        return render(request, 'uilajillagaa/category_topics.html', context)
    
    except Product.DoesNotExist:
        logger.error(f"Product does not exist. Category_slug: {category_slug}, Product_slug: {product_slug}")
        return HttpResponseNotFound("Product not found")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return HttpResponseServerError("An unexpected error occurred.")
   
def search_result(request):
    return render(request, "search-result.html")
def category_topics(request, category_slug):
    selected_category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=selected_category)
    count = products.count()
    
    # Change the number 2 to the desired number of products per page
    paginator = Paginator(products, 4)  # Adjust the number as needed

    page = request.GET.get("page")
    
    try:
        paged_products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paged_products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paged_products = paginator.page(paginator.num_pages)

    context = {
        'selected_category': selected_category,
        'products': paged_products,
        'count': count,
    }

    return render(request, "uilajillagaa/category_topics.html", context)
def product_list(request, category=None):
    products = Product.objects.all()
    return render(request, "uilajillagaa/product_list.html", {'products': products})
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Бүтээгдэхүүнийг амжилттай нэмлээ.')
            return redirect('product_detail', category_slug=form.instance.category.slug, product_slug=form.instance.slug)  # Redirect to a success page
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'uilajillagaa/add_product.html', context)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            form.save()
            messages.success(request, 'Бүтээгдэхүүн амжилттай заслаа.')
            return redirect('product_detail', pk=product.pk)
        else:
            form = ProductForm(instance=product)
        context = {'form': form, 'product': product}
        return render(request, 'uilajillagaa/add_product.html', context)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')
def home(request):
    categories = Category.objects.all()

    # Establish a connection to the PostgreSQL database

    # Create a cursor to execute SQL           
    cur = connect.cursor()

    # Execute a sample SQL query (replace it with your actual query)
    cur.execute("SELECT * FROM categoty_product")
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
