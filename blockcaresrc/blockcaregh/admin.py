from django.contrib import admin
from blockcaregh.models import Manufacturer, Pharmacy, Distributor, Product

admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Pharmacy)
admin.site.register(Distributor)