from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, default='Advil')
    serial = models.IntegerField(default='12332109878')

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    email = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    registrar_id = models.CharField(max_length=25)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Pharmacy(models.Model):
    name = models.CharField(max_length =20)
    registrar_id = models.CharField(max_length=11)
    manufacturer = models.ManyToManyField(Manufacturer)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Pharmacie'


class Distributor(models.Model):
    name =models.CharField(max_length =20)
    email = models.CharField(max_length =25)
    registrar_id = models.CharField(max_length=11)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    pharmacy = models.ManyToManyField(Pharmacy)
    product = models.ManyToManyField(Product)

    def __str__ (self):
        return self.name
