from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='food'),
    path('drinks/', views.drinks, name='drink'),
    path('news/', views.news, name='newfood'),
    path('foods/', views.foods, name='fastfood'),
    path('card/',views.card , name = 'card_url'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', views.edit_cart_item, name='edit_cart_item'),
    path('add_to_cart/<pk>' , views.add_to_cart , name = 'add_to_cart_url'),
    path('create_order' , views.create_order , name = 'create_order'),
]