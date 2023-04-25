"""Py_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import django
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from Py_2.settings import STATICFILES_DIRS, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from django.contrib import admin
from django.urls import include, path, re_path
from APP.views import *
from django.views.static import serve

handler404 = 'APP.views.custom_handler404'
admin.autodiscover()

urlpatterns = [
    path('products/<int:ke>/', fil_ke, name='fil_ke'),
    path('prochee/', include('APP.urls')),
    path('categories/', json_s),
    path('categories/<str:keys>/', categories_view),
    path('list/', jsoni),
    path('', nach, name='home'),
    path('product//buy', add),
    path('products/thx/', thx, name='thx'),
    path('add_product/', add_product, name='add_product'),
    path('add_category/', add_category, name='add_category'),
    path('products/', productsi, name='products'),
    path('admin/', admin.site.urls),
    re_path(r'^products/(?P<document_root>\d+)/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^products/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)