from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('customer/',views.cdash,name='cdash'),
    path('rsearch/',views.rsearch,name='rsearch'),
    path('restaurant/<int:restaurant_id>',views.restaurant,name='restaurant'),
    path('psearch/',views.psearch,name='psearch'),
    path('logout/',views.logout,name='logout'),
    path('category/<int:category_id>',views.category,name='category'),
    path('catsearch/',views.catsearch,name='catsearch'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('order/',views.order,name='order'),
    path('place_order/',views.place_order,name='place_order'),
    
]