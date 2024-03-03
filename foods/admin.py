from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Fastfoods)
admin.site.register(Drinks)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderProduct)