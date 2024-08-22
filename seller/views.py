from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponse
# Create your views here.
def sdash(request):
    if 'seller' in request.session:
        seller_id=request.session.get('seller')
        seller_object=Seller.objects.get(id=seller_id)
        context={
            'seller_object':seller_object
        }
    return render(request,'seller/sdash.html',context)

def addproduct(request):
    if 'seller' in request.session:
        all_category=Category.objects.all()
        seller_id=request.session.get('seller')
        seller_object=Seller.objects.get(id=seller_id)
        if request.method=='POST':
            name=request.POST['name']
            image=request.FILES['image']
            price=request.POST['price']
            discription=request.POST['discription']
            category_id=request.POST['category']
            category=Category.objects.get(id=category_id)
            seller=Product(product_name=name,image=image,price=price,discription=discription,restaurant=seller_object,category=category)
            seller.save()
        return render(request,'seller/addproduct.html',{'category':all_category})
    else:
        return render(request,'authentication/slogin.html')

def viewproduct(request):
    if 'seller' in request.session:
        seller_id=request.session.get('seller')
        seller_object=Seller.objects.get(id=seller_id)
        products=Product.objects.filter(restaurant=seller_object)
        return render(request,'seller/viewproduct.html',{'pdts':products})
    else:
        return render(request,'authentication/slogin.html')
        
def updatepdt(request,product_id):
    single_product=Product.objects.get(id=product_id)
    old_image=single_product.image
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        discription=request.POST['discription']
        if  request.FILES['image']:
            image_new=request.FILES['image']
            single_product.image=image_new
        else:
            single_product.image=old_image

        single_product.product_name=name
        single_product.price=price
        single_product.discription=discription
        single_product.save()
        return redirect('seller:viewproduct')
    return render(request,'seller/updatepdt.html',{'single_product':single_product})  

def deletepdt(request,product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('seller:viewproduct')  

def logout(request):
     if 'seller' in request.session:
          del request.session['seller']
          return render(request,'authentication/index.html')
     else:
          return render(request,'authentication/index.html')
     
def view_orders(request):
    if 'seller' in request.session:
        seller_id=request.session.get('seller')
        seller_object=Seller.objects.get(id=seller_id)
        orders=Order.objects.filter(product__restaurant=seller_object)
        return render(request,'seller/view_orders.html',{'orders':orders})
    else:
        return render(request,'authentication/slogin.html')
    
def cancel_order(request,order_id):
    Order.objects.get(id=order_id).delete()
    return redirect('seller:view_orders') 

def complete_order(request,order_id):
    Order.objects.get(id=order_id).delete()
    return redirect('seller:view_orders') 