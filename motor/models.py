from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('jeans', 'Jeans'),
        ('tshirts', 'T-shirts'),
        ('sweatpants', 'Sweatpants'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/images')
    company = models.CharField(max_length=100, default="Default Company")
    description = models.TextField(default="No description provided")
    

    def __str__(self):
        return self.name
    

# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def subtotal(self):
#         return self.quantity * self.product.price

# class Cart(models.Model):
#     items = models.ManyToManyField(CartItem)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def total(self):
#         return sum(item.subtotal() for item in self.items.all())

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())  # Access related CartItems

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE, null=True)  # Link to a specific Cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.product.price

