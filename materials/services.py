from config.settings import STRIPE_SECRET_KEY
import stripe
from users.models import Payment

stripe.api_key = STRIPE_SECRET_KEY


def create_link_for_payment(payment_sum):
    '''Создает продукт, цену и ссылку на оплату в страйпе'''
    product = stripe.Product.create(name='course')

    product_price = stripe.Price.create(
        unit_amount=payment_sum,
        currency="usd",
        product=product.get("id"),
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": product_price.get("id"), "quantity": 1}],
    )

    return payment_link.get("url")
