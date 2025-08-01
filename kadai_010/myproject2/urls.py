"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from crud import views
from crud.views import ProductCreateView
from django.contrib import admin
from django.urls import path
from crud.views import ProductListView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name='top'),
    path('crud/', views.ProductListView.as_view(), name='list'),
    path('crud/new/', ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    path('crud/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]
