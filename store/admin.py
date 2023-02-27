from django.contrib import admin
from .models.product import Product
from .models.category import category
from .models.customer import Customer
from .models.orders import Order

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']

class AdminOrder(admin.ModelAdmin):
    model=Product
    model=Customer
    list_display = ['get_product','get_cname', 'quantity', 'price', 'address','phone','status','date']

    def get_product(self,obj):
        return obj.product.name
    
    def get_cname(self,obj):
        return obj.customer.first_name




admin.site.register(Product, AdminProduct)
admin.site.register(category, AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)  
