from django.urls import path
from . import order_views

urlpatterns = [
    path('create_order', order_views.create_order, name='contact'),
    path('order_confirmation', order_views.order_confirmation, name='order_confirm')
]