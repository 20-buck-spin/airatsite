from rest_framework.serializers import ModelSerializer
from .models import Order, PaymentInvoice


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
