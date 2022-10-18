from django.contrib import admin
from.models import Firm, Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','firm', 'volume', 'colour','description', 'amount', 'price' )
    list_filter = ('firm','type')


admin.site.register(Firm)
admin.site.register(Product, ProductAdmin)