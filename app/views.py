from django.shortcuts import render, redirect
from .form import AddSupplyForm, AddShipmentForm
from . import services


# Create your views here.
def models_tv(request):
    data = services.get_models_tv()
    return render(request=request, template_name="app/models_tv.html", context=data)


def index(request):
    return render(request=request, template_name="app/index.html")


def shipments(request):
    data = services.get_shipments()
    return render(request=request, template_name="app/shipments.html", context=data)


def supply(request):
    data = services.get_supplies()
    return render(request=request, template_name="app/supply.html", context=data)


def stocks(request):
    data = services.get_stocks()
    return render(request=request, template_name="app/stocks.html", context=data)


def add_supply_form(request):
    if request.method == "POST":
        form = AddSupplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # services.add_stock(post.count, post.tv, post.storehouse)
            post.save()
            return redirect('supply')
    else:
        form = AddSupplyForm()
    return render(request=request, template_name="app/form_add_supply.html", context={'form': form})


def add_shipment_form(request):
    if request.method == "POST":
        form = AddShipmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # services.update_stock(post.count, post.tv, post.storehouse)
            post.save()
            return redirect('shipments')
    else:
        form = AddShipmentForm()
    return render(request=request, template_name="app/form_add_shipment.html", context={'form': form})
