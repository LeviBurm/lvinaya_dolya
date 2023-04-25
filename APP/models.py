from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=128, default='имя не присвоено', unique=True)
    category_picture = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    product_ves = models.IntegerField(max_length=200)
    product_price = models.IntegerField(max_length=200)
    product_godnost = models.IntegerField(max_length=200)
    product_volume = models.IntegerField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to="media/", blank=True)
    ssilka = models.URLField(max_length=200, default='http://127.0.0.1:8000/products/')

    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"