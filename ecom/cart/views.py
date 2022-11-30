from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product
from .models import Cart,Cartitem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart    


def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    print(product)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        print(cart,"hhii")
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item=Cartitem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            
            cart_item.quantity +=1
        cart_item.save()
    except Cartitem.DoesNotExist:
        print("hello")
        cart_item=Cartitem.objects.create(product=product,cart=cart,quantity=1)
        cart_item.save()
        
    return redirect ("cart:cart_detail")

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=Cartitem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price*cart_item.quantity)
            counter=cart_item.quantity
            print(cart_items,"jii")
    except ObjectDoesNotExist:
        pass
    
    
    context={
        'cart_items':cart_items,
        'total':total,
        'counter':counter   
    }
    
    return render(request,'shop/cart.html',context)
            

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product= get_object_or_404(Product,id=product_id)
    cart_item = Cartitem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
        
    return redirect('cart:cart_detail')        
    
def removef(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product= get_object_or_404(Product,id=product_id)
    cart_item = Cartitem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
            