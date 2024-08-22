from django.urls import path
from . import views
app_name='seller'
urlpatterns=[
    path('seller/',views.sdash,name='sdash'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('updatepdt/<int:product_id>',views.updatepdt,name='updatepdt'),
    path('deletepdt/<int:product_id>',views.deletepdt,name='deletepdt'),
    path('logout/',views.logout,name='logout'),
    path('view_orders/',views.view_orders,name='view_orders'),
    path('cancel_order/<int:order_id>',views.cancel_order,name='cancel_order'),
    path('complete_order/<int:order_id>',views.complete_order,name='complete_order'),
]