
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.about import About
from .views.contact import Contact
from .views .cart import Cart
from .views.checkout import Checkout
from .views.orders import OrderView
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()), name='orders'),
    path('about',About, name='about'),
    path('contact',Contact, name='contact'),
]
