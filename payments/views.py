from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from orders.models import Order

@api_view(['POST'])
def receive_payment_callback(request, invoice_id, status):
    data = dict(request.data)
    return Response({'status': "success"})
