from abc import ABC, abstractmethod
from ..models import PaymentInvoice


class BasePaymentProvider(ABC):
    @abstractmethod
    def get_payment_link(self, invoice: PaymentInvoice):
        # prepare the request, get the request and send the url back
        pass

    @abstractmethod
    def process_payment_status_webhook(self, request, invoice: PaymentInvoice):
        # decrypt the response, change status of invoice if needed
        pass

    @abstractmethod
    def __init__(self, params: dict):
        pass
