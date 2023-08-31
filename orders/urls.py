from django.urls import path
from . import views

urlpatterns = [
    path('create_order', views.create_order, name='contact'),
    path('order_confirmation', views.order_confirmation, name='order_confirm'),
    path('<str:id>/payment', views.order_payment, name='order_payment')
]