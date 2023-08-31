from decimal import Decimal
from random import choices

from django.db import models
import uuid


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=100, verbose_name='ФИО')
    client_telephone = models.CharField(max_length=100, verbose_name="Номер Телефона")
    client_email = models.EmailField(max_length=100, verbose_name="Почта")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True, blank=True, default=Decimal("0.00"),
                                 verbose_name="Сумма"
                                 )

    order_statuses = (('0', 'Новый'),
                      ('1', 'В ожидании оплаты'),
                      ('2', 'Оплачено'),
                      ('3', 'В работе'),
                      ('4', 'Успешено'),
                      ('5', 'Отменено')
                      )
    order_status = models.CharField(max_length=2, choices=order_statuses, default='0', verbose_name="Статус")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


    def gen_payment_link(self):
        return f"https://www.host.com/order/{self.id}/payment"
