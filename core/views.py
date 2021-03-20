from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import CreateUserForm
# Create your views here.

def RegisterPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Successfully created')
            return redirect('/login/')
            
    context = {
        'form': form,
    }
    return render(request,'core/register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                print("Customer :", request.user.customer)
            except ObjectDoesNotExist:
                request.user.customer = Customer.objects.create(user=user, name=username,email=user.email)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {

    }
    return render(request,'core/login.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('/login/')


def Build(request):

    context = {

    }
    return render(request,'core/build.html', context)


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    
    context = {
        'products': products,
        'cartItems': cartItems,
    }
    return render(request,'core/store.html', context)


def product(request, id):
    data = cartData(request)
    product = Product.objects.get(id=id)
    cartItems = data['cartItems']

    context = {
        'product': product,
        'cartItems': cartItems
    }
    return render(request,'core/product.html',context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }

    return render(request,'core/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action :', action , 'ProductId :', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was Added', safe=False)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request,'core/checkout.html', context)


def processsOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    print ("\n\n Total :", total, "type :", type(total) )
    print ("\n\n cart Total :", order.get_cart_total, "type :", type(order.get_cart_total) )
    print('\n\n CHECKING ORDER \n\n')
    if float(total) == float(order.get_cart_total):
        print("total (" + str(total) + ") == cart Total (" + str(order.get_cart_total) + ") is", float(total) == float(order.get_cart_total))
        order.complete = True
        print('\n\n ORDER COMPLETE \n\n')
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            address2 = data['shipping']['address1'],
            city = data['shipping']['city'],
            number = data['shipping']['number']
        )

    return JsonResponse('Payment Complete!', safe=False)


