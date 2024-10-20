from django.urls import path
from .views import (
    index, product_list, add_product, delete_product,
    staff_signup, staff_login, staff_logout,
    home, login_view, logout_view, register_view,
    add_to_cart, cart_view, delete_cart_item,
    ProductDetailView, edit_product ,about # Make sure to import edit_product
)
from .views import create_order
from .views import update_cart
from .views import search_view
from .views import search_viewH
app_name = 'accounts'  # Make sure to set the app name

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('staff/signup/', staff_signup, name='staff_signup'),
    path('staff/login/', staff_login, name='staff_login'),
    path('staff/logout/', staff_logout, name='staff_logout'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/delete/<int:item_id>/', delete_cart_item, name='delete_cart_item'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('create_order/', create_order, name='create_order'),
    path('update_cart/', update_cart, name='update_cart'),
    path('search/', search_view, name='search'),
    path('searched/', search_viewH, name='searched'),
    path('about/',about, name='about')
    
    
    # Use the imported view
]
