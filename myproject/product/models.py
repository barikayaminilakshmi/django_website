from django.db import models


class Product(models.Model):
    pro_name = models.CharField(max_length=20)
    pro_id = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.pro_name