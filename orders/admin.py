from decimal import Decimal

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Order
from .tasks import send_order_payment_email
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = "created_datetime"
    list_display = ["id", "created_datetime", "client_email", "client_name", "client_telephone", "order_status"]
    search_fields = ['id', 'client_email']
    list_filter = ["order_status"]
    search_help_text = "Поиск по ID или почте клента"

    change_form_template = "order_admin_changepage_buttons.html"

    def response_change(self, request, obj):
        if "_send_payment_link" in request.POST:
            if not obj.amount > Decimal("0.00"):
                self.message_user(request, "Сумма заказа должен быть больше 0", level=messages.ERROR)
            else:
                # Send email to user with link for payment
                obj.order_status = "1"
                send_order_payment_email(obj)
                self.message_user(request, "Отправлен клиенту счет на оплату")
        elif "_mark_in_progress" in request.POST:
            obj.order_status = '3'
            self.message_user(request, "Заказ помечен как в процессе")

        elif "_mark_success" in request.POST:
            obj.order_status = '4'
            self.message_user(request, "Заказ помечен как успешно")

        elif "_mark_cancelled" in request.POST:
            obj.order_status = '5'
            self.message_user(request, "Заказ помечен как отменено")

        else:
            return super().response_change(request, obj)

        obj.save()
        return HttpResponseRedirect(".")
