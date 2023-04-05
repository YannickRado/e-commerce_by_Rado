from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ecommerce.models import Product, Cart, Order
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        products = Product.object.filter(tittle__icontains=item_name)
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'ecommerce/index.html', context={"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'ecommerce/detail.html', context={"product": product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 ordered=False,
                                                 product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quntity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'ecommerce/cart.html', context={"orders": cart.orders.all()})

def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.delete()

    return redirect('index')
