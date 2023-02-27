from django.shortcuts import render, redirect
from store.models.customer import Customer
from django. views import View
from store .models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        product = Product.get_product_by_id(ids)
        return render(request, 'cart.html',{'products':product})
