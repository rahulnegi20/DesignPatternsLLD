

#TARGET INTERFACE

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass



# Implement an Existing Payment Processor

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing payment of ${amount} through PayPal.")



#  Integrate a New Payment Gateway (Incompatible Interface)

class StripePayment:
    def make_payment(self, amount: float) -> None:
        print(f"Processing payment of ${amount} through Stripe.")


# Since StripePayment doesn’t implement the process_payment method, we cannot directly use it as a PaymentProcessor.s



class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_payment: StripePayment):
        self.stripe_payment = stripe_payment

    def process_payment(self, amount: float) -> None:
        # Adapt the `process_payment` method to call `make_payment`
        self.stripe_payment.make_payment(amount)


# Create an Adapter (StripeAdapter) to Adapt StripePayment to 




# USAGE

# Existing payment processor
paypal_processor = PayPalProcessor()
paypal_processor.process_payment(50.0)

# New payment processor using the adapter
stripe_payment = StripePayment()
stripe_processor = StripeAdapter(stripe_payment)
stripe_processor.process_payment(75.0)
