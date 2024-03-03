from django.db import models

# Create your models here.


class Fastfoods(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    images = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Drinks(models.Model):
    title = models.CharField(max_length=255)
    inst = models.CharField(max_length=40)
    face = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title




class CartItem(models.Model):
    product = models.ForeignKey(Fastfoods,on_delete = models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.customer)

    def total_price(self):
        return self.product.price * self.quantity




class Order(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    total_price = models.IntegerField()


    def __str__(self):
        return 'Order # %s' % (str(self.id))


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Fastfoods, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '%s x%s - %s' % (self.product, self.amount, self.order.customer.username)
