from django.urls import path
from .views import receive_payment_callback

urlpatterns = [
    path("payments/<invoice_id:str>/<status:str>", receive_payment_callback)
]