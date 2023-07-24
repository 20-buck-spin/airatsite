from django.urls import path
from . import views

urlpatterns = [
    # Page views
    path('', views.index, name='index'),
    path('about', views.about_us, name='about'),
]