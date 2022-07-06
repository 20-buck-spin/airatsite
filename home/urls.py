from django.urls import path
from . import views

urlpatterns = [
    # Page views
    path('', views.index, name='index'),


    # Сontact form
    path('contact', views.contact, name='contact'),
]