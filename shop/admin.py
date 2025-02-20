from django.contrib import admin
from .models import *
class ProductAdmin(admin.ModelAdmin):
  list_display=['id','name','price']
admin.site.register(Product,ProductAdmin)

admin.site.register(Category)
admin.site.register(CartItem)