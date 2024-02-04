from django.shortcuts import render, get_object_or_404
from .models import Duureg
from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from .forms import AddressForm

def address_list(request):
    addresss = Address.objects.all()
    context = {
        'addresss': addresss
        }
    return render(request, 'hayg/duuregs.html', context)

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
    addresss = get_object_or_404(Address, pk=pk)
    addresss.delete()
    return redirect('address_list')

def duureg_list(request):
    duuregs = Duureg.objects.all()
    context = {
        'duuregs': duuregs,
    }
    return render(request, 'hayg/duuregs.html', context)

def detail(request, duureg_slug):
    duureg = get_object_or_404(Duureg, slug=duureg_slug)
    context = {
        'duureg': duureg,  # Change the variable name to 'product'
    }
    return render(request, 'hayg/detail.html', context)
