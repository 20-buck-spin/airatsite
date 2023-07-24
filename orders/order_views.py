from rest_framework.response import Response

from .models import Order
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import OrderSerializer


@api_view(['POST'])
def create_order(request):
    try:
        client_name = request.data.get('name')
        client_email = request.data.get('email')
        client_phone_no = request.data.get('phone_no')
        description = request.data.get('description')
    except KeyError:
        return Response({'status': "Error", 'errors': "Invalid data"})

    data = {'client_name': client_name, 'client_email': client_email,
         'client_telephone': client_phone_no, 'description': description}

    print(data)
    new_order_serializer = OrderSerializer(data=data)

    if new_order_serializer.is_valid():
        # Send email notification
        return Response({'status': 'Success'})
    else:
        return Response({'status': "Error", 'errors': new_order_serializer.errors})


def order_confirmation(request):
    return render(request, 'generic_title_message.html', context={'message': {
        'title': 'Обращение получено!',
        'message': 'Мы получили ваше обращение! В течение 1-2 рабочнх дней вы получите обратную связь! '
    }})

