import stripe

stripe.api_key = 'sk_test_51I9ulJIwEKXXjOJ0ldupNrZDEPrWb7DnfchUWKrfKb1PbjjPlTuGs6bYVekt1lkCDADsg9VOWmjEc26Pigo3ucoh0010ni4cg8'

stripe.PaymentIntent.create(
    amount=1000
    currency='usd',
    payment_method_types=['card'],
    recipient_email='rhoades.webdev@gmail.com'
)