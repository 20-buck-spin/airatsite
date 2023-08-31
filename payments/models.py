from django.db import models
import uuid
from orders.models import Order


def payment_page_logo_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/payment_providers/{id}/logo.{extension}
    return f"payment_providers/{instance.name}/logo.{filename.split('.')[-1]}"


# Create your models here.
class PaymentProvider(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=payment_page_logo_upload)
    description = models.TextField()
    priority = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    ip_whitelist = models.TextField()
    params = models.JSONField()

    class Meta:
        ordering = ('priority', 'id')
        verbose_name = 'Платежное решение'
        verbose_name_plural = "Платежные решения"


class PaymentInvoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    payment_provider = models.ForeignKey(PaymentProvider, on_delete=models.PROTECT)
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_datetime = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    PAYMENT_STATUSES = (('0', 'Новый'),
                        ('1', 'Успешен'),
                        ('2', 'Неуспешен'),
                        ('3', 'Истекший'),
                        ('4', 'Отменен'),
                        ('5', 'В ожидании'))

    status = models.CharField(max_length=2, choices=PAYMENT_STATUSES, default='0', verbose_name="Статус")
    request_data = models.JSONField()
    response_data = models.JSONField()

    class Meta:
        verbose_name = 'Инвойс оплаты'
        verbose_name_plural = "Инвойсы оплаты"