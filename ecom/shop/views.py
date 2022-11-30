from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage 

from django.shortcuts import render
from shop .models import Product
from django.db.models import Q




def index(request):
    return render(request, 'index.html')

def allproduct(request,c_slug=None):
    c_page= None
    products_list=None

    if c_slug!= None:
        c_page= get_object_or_404(Category,slug=c_slug)
        products_list = Product.objects.all().filter(category = c_page,available=True)
    else:
        products_list =Product.objects.all().filter(available=True) 
        paginator=Paginator(products_list,5) 
    try:
        page=int(request.GET.get('page','1'))
        
    except:
        page=1  
        
    try:
        products=paginator.page(page)  
        
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
 
    context={
        'c_page':c_page,
        'products':products
        
    }
      

    return render(request,"shop/category.html",context)
    
def Productdetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
        print(product)
    
    except Exception as e:
        raise e     
    
    context={

        'products':product
        
    }
    
    return render(request,"shop/product.html",context)
    
    
    

    