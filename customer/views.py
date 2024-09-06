from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponse
from authentication.models import*
from seller.models import*
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
# Create your views here.
def cdash(request):
     if 'customer' in request.session:
          restaurant=Seller.objects.all()
          category=Category.objects.all()
          return render(request,'customer/cdash.html',{'seller':restaurant,'category':category})
     else:
          return render(request,'authentication/clogin.html')
     
def rsearch(request):
     if 'keyword' in request.GET:
          keyword=request.GET['keyword']
          if keyword:
               restaurant=Seller.objects.filter(hname__icontains=keyword)  
          context={
               'seller':restaurant,
          }   
     return render(request,'customer/cdash.html',context)  

def restaurant(request,restaurant_id):
     restaurant=Seller.objects.get(id=restaurant_id)
     product=Product.objects.filter(restaurant=restaurant)
     category=Category.objects.all()
     context={
          'seller':restaurant,
          'product':product,
          'category':category
     }
     return render(request,'customer/restaurant.html',context)

def psearch(request):
     if 'keyword' in request.GET:
          keyword=request.GET['keyword']
          if keyword:
               product=Product.objects.filter(product_name__icontains=keyword)  
          context={
               'pdts':product,
          }   
     return render(request,'customer/restaurant.html',context)   

def logout(request):
     if 'customer' in request.session:
          del request.session['customer']
          return render(request,'authentication/index.html')
     else:
          return render(request,'authentication/index.html')
     
def category(request,category_id):
     category=Category.objects.get(id=category_id)
     product=Product.objects.filter(category=category)
     all_category=Category.objects.all()
     
     context={
          'category':category,
          'product':product,
          'all_category':all_category,
     }
     
     return render(request,'customer/category.html',context)

def catsearch(request):
     if 'keyword' in request.GET:
          keyword=request.GET['keyword']
          if keyword:
               product=Product.objects.filter(product_name__icontains=keyword)  
          context={
               'pdts':product,
          }   
     return render(request,'customer/restaurant.html',context) 

def add_to_cart(request,product_id):
 if 'customer' in request.session:
     c_id=request.session.get('customer')
     customer=Customer.objects.get(id=c_id)

     if request.method=='POST':
         product=Product.objects.get(id=product_id)
         cart_item,created=Cart.objects.get_or_create(product=product,customer=customer)
         if not created:
              cart_item.quantity+=1
              cart_item.save()
         return redirect('customer:cart')

def cart(request):
     if 'customer' in request.session:
          category=Category.objects.all()
          cdetails=request.session.get('customer')
          customer=Customer.objects.get(id=cdetails)
          cartitems=Cart.objects.filter(customer=customer)
          grandtotal=0
          for item in cartitems:
               item_total=item.product.price*item.quantity
               grandtotal+=item_total
          context={
                    'cartitems':cartitems,
                    'grandtotal':grandtotal,
                    'category':category
               }
          return render(request,'customer/cart.html',context)
     else:
          return render(request,'authentication/index.html')
     
def remove_from_cart(request,product_id):
     product=Product.objects.get(id=product_id)
     cart_items=Cart.objects.get(product=product)
     cart_items.delete()
     return redirect('customer:cart')

def order(request):
     if 'customer' in request.session:
          category=Category.objects.all()
          cdetails=request.session.get('customer')
          customer=Customer.objects.get(id=cdetails)
          cartitems=Cart.objects.filter(customer=customer)
          grandtotal=0
          for item in cartitems:
               item_total=item.product.price*item.quantity
               grandtotal+=item_total
          context={
                    'cartitems':cartitems,
                    'grandtotal':grandtotal,
                    'category':category,
                    'customer':customer,
               }
          return render(request,'customer/order.html',context)
     else:
          return render(request,'authentication/index.html')
     
def place_order(request):
     if 'customer' in request.session:
          cdetails=request.session.get('customer')
          customer=Customer.objects.get(id=cdetails)
          cartitems=Cart.objects.filter(customer=customer)
        
          for item in cartitems:
               Order.objects.create(
                    customer=item.customer,
                    product=item.product,
                    quantity=item.quantity
               )
        
          cartitems.delete()
        
          return render(request,'customer/order_placed.html')
     else:
          return render(request, 'authentication/index.html')