from django.urls import path
from .views import login_view
from .views import velog

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('login/',login_view, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('vendor/',views.vendor, name='vendor'),
    path('signup/', views.signup, name='signup'),
   
    path('velog/',velog, name='velog'),
    path('add/', views.add_product, name='add_product'),
    
    
    
]
