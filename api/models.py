from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "brand"
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='order_brand')
    customer_name = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    price_total = models.FloatField(default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.customer_name)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price =models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.name)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item_product')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item_order')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orderitems"
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return str(self.product)


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='delivery_order')
    shipped = models.BooleanField(default=False)
    products = models.ManyToManyField("DeliveredItem", related_name='delivery_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "deliveries"
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

    def __str__(self):
        return str(self.order)


class DeliveredItem(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='delivered_products')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "delivereditems"
        verbose_name = "Delivered Item"
        verbose_name_plural = "Delivered Items"

    def __str__(self):
        return str(self.product_name)
