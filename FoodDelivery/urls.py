from FoodDelivery.views import login,auth_view,logout,Menu,Register,adduser_details,Cart,Transaction,Order,MyAccount,Delete,Edit,MyOrders,AboutUs,viewproducts,vieworders,deleteproduct,updateproduct,addproduct
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    url(r'^login/$',login),
    url(r'^auth/$',auth_view),
    url(r'^Menu/$',Menu),
    url(r'^Cart/$',Cart),
    url(r'^Register/$',Register),
    url(r'^adduser_details/$',adduser_details),
    url(r'^logout/$',logout),
    url(r'^Transaction/$',Transaction),
    url(r'^Order/$',Order),
    url(r'^MyAccount/$',MyAccount),
    url(r'^Edit/$',Edit),
    url(r'^Delete/$',Delete),
    url(r'^MyOrders/$',MyOrders),
    url(r'^AboutUs/$',AboutUs),
    url(r'^viewproducts/$',viewproducts),
    url(r'^vieworders/$',vieworders),
    url(r'^updateproduct/$',updateproduct),
    url(r'^deleteproduct/$',deleteproduct),
    url(r'^addproduct/$',addproduct),
]
