from random import choices

from django.db import models


# Create your models here.
class Order(models.Model):
    client_name = models.CharField(max_length=100)
    client_telephone = models.IntegerField(max_length=100)
    client_email = models.EmailField(max_length=100)
    description = models.TextField(null=True, blank=True)


PAYMENT_STATUSES = (('0', 'Initialized'),
                    ('1', 'Success'),
                    ('2', 'Failed'),
                    ('3', 'Expired'),
                    ('4', 'Cancelled'),
                    ('5', 'Pending'))


class PaymentInvoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=PAYMENT_STATUSES)

