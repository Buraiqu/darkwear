from django.urls import path
from . import views
app_name='seller'
urlpatterns = [
    path('',views.seller_home,name = 'shome'),
    path('viewproducts',views.seller_products,name = 'viewproducts'),
    path('product_variant',views.seller_variant,name = 'variant'),
    path('changepassword',views.seller_change_password,name = 'changepassword'),
    path('stockupdate',views.seller_update_stock,name = 'stockupdate'),
    path('stock_up',views.seller_stock_up,name = 'stock_up'),
    path('add_stock',views.seller_add_stock,name = 'add_stock'),
    path('profile',views.seller_profile,name = 'profile')
]           