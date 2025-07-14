
# Step 1: Define the Strategy Interface

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Step 2: Implement Concrete Strategies

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, card_holder: str, cvv: str):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv

    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount} for {self.card_holder}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount} for {self.email}")

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        print(f"Processing crypto payment of ${amount} to wallet {self.wallet_address}")


# Step 3: Create a Context Class (ShoppingCart)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: str, price: float) -> None:
        self.items.append((item, price))

    def calculate_total(self) -> float:
        return sum(price for _, price in self.items)

    def pay(self, payment_strategy: PaymentStrategy) -> None:
        amount = self.calculate_total()
        payment_strategy.pay(amount)


# Create a shopping cart and add some items
cart = ShoppingCart()
cart.add_item("Laptop", 1500)
cart.add_item("Phone", 800)

# Choose a payment strategy at runtime
print("\nPaying with Credit Card:")
credit_card_payment = CreditCardPayment("1234-5678-9876-5432", "John Doe", "123")
cart.pay(credit_card_payment)

print("\nPaying with PayPal:")
paypal_payment = PayPalPayment("john@example.com")
cart.pay(paypal_payment)

print("\nPaying with Cryptocurrency:")
crypto_payment = CryptoPayment("1A2b3C4d5E6f7G8h9I0jK")
cart.pay(crypto_payment)
