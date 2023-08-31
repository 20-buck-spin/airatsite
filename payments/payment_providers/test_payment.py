from .base_class import BasePaymentProvider
from ..models import PaymentInvoice


class TestPayment(BasePaymentProvider):

    def __init__(self, params: dict):
        self.param1 = params.get('param1', '123')
        self.param2 = params.get('param2', '123')
        self.param3 = params.get('param3', '123')
        self.param4 = params.get('param4', '123')

    def get_payment_link(self, invoice: PaymentInvoice):
        # prepare the request, get the request and send the url back

        return "https://google.com"

    def process_payment_status_webhook(self, request, invoice: PaymentInvoice):
        # decrypt the response, change status of invoice if needed
        return invoice
