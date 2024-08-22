from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponse
# Create your views here.
def Index(request):
    return render(request,'authentication/index.html')
def clogin(request):
     if request.method=='POST':
            email=request.POST['uname']
            password=request.POST['password']
            
            try:
               cust=Customer.objects.get(email=email,password=password)
               request.session['customer']=cust.id
               return redirect('customer:cdash')          
            except:
               return render(request,'authentication/clogin.html',{'msg':'invalid email or password'})
     return render(request,'authentication/clogin.html')
def slogin(request):
     if request.method=='POST':
            email=request.POST['uname']
            password=request.POST['password']
            try:
               sell=Seller.objects.get(email=email,password=password)
               request.session['seller']=sell.id
               return redirect('seller:sdash')            
            except:
               return render(request,'authentication/slogin.html',{'msg':'invalid email or password'})
     return render(request,'authentication/slogin.html')
def cregister(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        address=request.POST['address']
        email=request.POST['email']
        mobile=request.POST['mobile']
        Password=request.POST['password']
        customer=Customer(fname=fname,lname=lname,address=address,email=email,mobile=mobile,password=Password)
        customer.save()
        print('saved')
        return redirect('authentication:clogin')
    return render(request,'authentication/cregister.html')
def sregister(request):
    if request.method=='POST':
        hname=request.POST['hname']
        address=request.POST['address']
        image=request.FILES.get('image')
        email=request.POST['email']
        mobile=request.POST['mobile']
        Password=request.POST['password']
        seller=Seller(hname=hname,address=address,image=image,email=email,mobile=mobile,password=Password)
        seller.save()
        return redirect('authentication:slogin')
    return render(request,'authentication/sregister.html')

def about(request):
    return render(request,'authentication/about.html')

def services(request):
    return render(request,'authentication/services.html')

def contact(request):
    return render(request,'authentication/contact.html')