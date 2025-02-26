"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop.views import home,register,login_page,logout_page,details,view_cart,add_to_cart
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('register/',register,name="reg"),
    path('login/',login_page,name="logIn"),
    path('logout/',logout_page,name="logOut"),
    path('details/<str:pk>/',details,name="details"),
    path('cart/',view_cart,name="cart"),
    path('add_to_cart/',add_to_cart,name="add_to_cart"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
