from django.contrib import admin
from .models import PaymentProvider, PaymentInvoice
from django.utils.html import mark_safe

# Register your models here.


@admin.register(PaymentInvoice)
class PaymentInvoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "created_datetime", "order", "updated_datetime", "status", "get_amount"]

    def get_amount(self, obj):
        return obj.order.amount

    get_amount.short_description = "Сумма"
    get_amount.admin_order_field = "order__amount"


@admin.register(PaymentProvider)
class PaymentProviderAdmin(admin.ModelAdmin):
    list_display = ["id", "logo_img", "name", "description", "priority", "is_active"]

    def logo_img(self, obj: PaymentProvider):
        return mark_safe(f"""
                <img src="{obj.logo.url}" width='40' height='40'>
                """)
