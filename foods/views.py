from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Fastfoods, Drinks , CartItem, Order, OrderProduct
from . import forms
from django.db.models import Q



def foods(request):
    search = request.GET.get('search')
    fastfood = Fastfoods.objects.all()
    print(search)
    if search:
        fastfood = fastfood.filter(Q(title__icontains=search))
    return render(request, 'fastfoods.html', {'foods':fastfood})


def drinks(request):
    search = request.GET.get('search')
    food_drinks = Drinks.objects.all()
    print(search)
    if search:
        food_drinks = food_drinks.filter(Q(title__icontains=search))
    return render(request, 'drinks.html', {'foods':food_drinks})

def news(request):
    food_news = news.objects.all()
    return render(request, 'news.html', {'foods':food_news})

def homepage(request):
    home_page = Fastfoods.objects.all()
    return render(request, 'homepage.html', {'foods':home_page})

def card(request):
    card_items = CartItem.objects.filter()
    total_price = sum([item.total_price() for item in card_items])
    total_quantity = sum([item.quantity for item in card_items])
    return render(request,'card.html',{'total_price':total_price,'cart_items':card_items,'total_quantity':total_quantity})

def delete_cart_item(request,pk):
  cart_item = CartItem.objects.get(pk=pk).delete()
  return redirect('foods:card_url')



def edit_cart_item(request, pk):
   cart_item = CartItem.objects.get(pk=pk)
   action = request.GET.get('action')

   if action == 'take' and cart_item.quantity > 0:
       if cart_item.quantity == 1:
           cart_item.delete()
           return redirect('foods:card_url')
       cart_item.quantity -= 1
       cart_item.save()
       return redirect('foods:card_url')
   cart_item.quantity += 1
   cart_item.save()
   return redirect('foods:card_url')



def create_order(request):
   cart_items = CartItem.objects.filter()
   total_price = sum([item.total_price() for item in cart_items])
   amount = sum([item.quantity for item in cart_items])

   form = forms.OrderForm(request.POST)
   if request.method == 'POST' and form.is_valid():
    order = Order.objects.create(
      address=request.POST.get('address'),
      phone=request.POST.get('phone'),
      total_price=total_price
    )
    for cart_item in cart_items:
      OrderProduct.objects.create(
        order=order,
        product=cart_item.product,
        amount=cart_item.quantity,
        total=cart_item.total_price())
      cart_items.delete()
      return redirect('foods:card_url')
      
   return render(request, 'order_creation_page.html', {
       'cart_items': cart_items,
       'total_price': total_price,
       'amount': amount,
       'form': form})

     


def add_to_cart(request, pk):
    kol = request.GET.get('kol')
    if not kol or not kol.isdigit():
        return redirect('foods:fastfood')
    kol = int(kol)
    if kol:
        product = Fastfoods.objects.get(pk=pk)
        cart_item = CartItem.objects.filter(product=product)
    if not cart_item:
        cart_item = CartItem.objects.create(product=product, quantity=kol)
        cart_item.save()
        return redirect('foods:fastfood')
    for item in cart_item:
        item.quantity = kol
        item.save()
        return redirect('foods:card_url')