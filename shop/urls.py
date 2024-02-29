"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from product.views import test_view, date_view, bye_view, main_view, product_list_view, \
    product_detail_view, create_product_view, create_review_view

from user.views import register_view, login_view, profile_view, logout_view, confirm_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('date/', date_view),
    path('bye/', bye_view),
    path('', main_view, name='main_view'),
    path('products/', product_list_view),
    path('products/<int:pk>/', product_detail_view),
    path('products/create/', create_product_view),
    path('products/<int:pk>/create_review/', create_review_view),

    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view'),
    path('confirm/', confirm_view, name='confirm_view'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
