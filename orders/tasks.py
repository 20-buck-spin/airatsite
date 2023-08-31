from django.core.mail import EmailMultiAlternatives

from .models import Order
from django.template.loader import get_template


# Not a celery task for now
def send_order_payment_email(order: Order):

    context = {"order": order}
    html_template = get_template('email_templates/order_payment_email_template.html')

    subject, from_email, to_email = "Заказ Принят! Оплатите его", "from@asd.com",order.client_email
    html_content = html_template.render(context)
    msg = EmailMultiAlternatives(subject, None, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    # msg.send()