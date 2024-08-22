from django.urls import path
from . import views
app_name='authentication'
urlpatterns=[
    path('',views.Index,name='index'),
    path('clogin/',views.clogin,name='clogin'),
    path('slogin/',views.slogin,name='slogin'),
    path('cregister/',views.cregister,name='cregister'),
    path('sregister/',views.sregister,name='sregister'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
]