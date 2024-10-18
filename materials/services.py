from config.settings import STRIPE_SECRET_KEY
import stripe

stripe.api_key = STRIPE_SECRET_KEY


def create_link_for_payment(course):
    '''Создает продукт, цену и ссылку на оплату в страйпе'''
    product = stripe.Product.create(name=course.name)

    price = stripe.Price.create(
        unit_amount=course.price*100,
        currency="usd",
        product=product.get("id"),
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": price.get("id"), "quantity": 1}],
    )

    return payment_link.get("url")
