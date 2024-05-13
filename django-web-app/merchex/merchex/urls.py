"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band_list'),
    path('bands/<int:band_id>/', views.band_detail, name='band_detail'),
    path('bands/add/', views.band_create, name='band_create'),
    path('bands/<int:band_id>/edit', views.band_edit, name='band_edit'),
    path('bands/<int:band_id>/delete', views.band_delete, name='band_delete'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/<int:contact_id>/edit', views.contact_edit, name='contact_edit'),
    path('contacts/<int:contact_id>/delete', views.contact_delete, name='contact_delete'),
    path('about-us/', views.about),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('email-sent/', views.email_sent, name='email_sent'),
]
