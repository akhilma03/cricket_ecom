from django.shortcuts import render
from shop .models import Product
from django.db.models import Q


# Create your views here.
def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET['q']
        products=Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'shop/search.html',{'query':query,'products':products})
    
    
    
                                        
        