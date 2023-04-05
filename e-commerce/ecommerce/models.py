from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from Site_ecommerce.settings import AUTH_USER_MODEL

"""
class Category(models.Model):
    name_cat = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
"""
"""
manana produit
- Nom
- Prix
- Quantité en stock
- description
- Images

"""

class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    price = models.FloatField(default=0.0) #prix
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
   # category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True) #image

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug}) #instence dans le slog

    """
    manana article
    -Utilisateur
    -Produit
    -Quantité
    -commandé ou non
    
    """

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quntity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quntity})"

"""
manana panier
-Utilisateur
-Articles
-Commandé ou non
-Date et heure de la commande
"""
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()

        super().delete(*args, **kwargs)

