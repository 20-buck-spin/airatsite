from django.http import HttpResponseRedirect
from rest_framework.response import Response

from .models import Order
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from payments.models import PaymentProvider


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
        new_order_serializer.save()
        return Response({'status': 'Success'})
    else:
        return Response({'status': "Error", 'errors': new_order_serializer.errors})


def order_confirmation(request):
    return render(request, 'generic_title_message.html', context={'message': {
        'title': 'Обращение получено!',
        'message': 'Мы получили ваше обращение! В течение 1-2 рабочнх дней вы получите обратную связь! '
    }})


def order_payment(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return render(request, 'error_page', context={'error': {
            "code": "404",
            "message": "Заказ не сущуествует"
        }})

    # Accept post method only for new or awaiting payment orders
    if request.method == 'GET' or order.order_status not in ["0", "1"]:
        payment_methods = PaymentProvider.objects.filter(is_active=True)
        context = {'order': order,
                   'payment_methods': payment_methods}
        return render(request, 'order_payment_page.html', context=context)

    if request.method == 'POST':
        # Get Url from payment provider/s
        return HttpResponseRedirect("asd")

