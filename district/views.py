from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from .forms import AddressForm

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'hayg/products.html', {'addresses': addresses})

def address_detail(request, pk):
    address = get_object_or_404(Address, pk=pk)
    return render(request, 'address_app/address_detail.html', {'address': address})

def address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm()
    return render(request, 'address_app/address_form.html', {'form': form})

def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm(instance=address)
    return render(request, 'address_app/address_form.html', {'form': form})

def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    address.delete()
    return redirect('address_list')

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'hayg/products.html', context)

def detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product,  # Change the variable name to 'product'
    }
    return render(request, 'hayg/detail.html', context)
