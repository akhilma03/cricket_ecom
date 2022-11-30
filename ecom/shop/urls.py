
from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    
    path('',views.allproduct, name="allproducts"),
    path('<slug:c_slug>/', views.allproduct, name="category"),
     path('<slug:c_slug>/<slug:product_slug>/', views.Productdetail, name="procat"),
 
   
]
