# Step 1: Define the Template Method in the Base Class

from abc import ABC, abstractmethod

class OrderProcessor(ABC):
    def process_order(self) -> None:
        self.select_item()
        self.payment()
        self.delivery()
        self.send_confirmation()

    def select_item(self) -> None:
        print("Item selected.")

    def send_confirmation(self) -> None:
        print("Order confirmation sent to customer.")

    @abstractmethod
    def payment(self) -> None:
        pass

    @abstractmethod
    def delivery(self) -> None:
        pass


# Step 2: Create Concrete Subclasses

class InStorePickupOrder(OrderProcessor):
    def payment(self) -> None:
        print("Processing in-store payment.")

    def delivery(self) -> None:
        print("Setting up in-store pickup.")

class HomeDeliveryOrder(OrderProcessor):
    def payment(self) -> None:
        print("Processing online payment.")

    def delivery(self) -> None:
        print("Shipping to home address.")

class InternationalDeliveryOrder(OrderProcessor):
    def payment(self) -> None:
        print("Processing international payment with additional fees.")

    def delivery(self) -> None:
        print("Shipping internationally with customs clearance.")

# Usage

# Process an in-store pickup order
print("In-Store Pickup Order:")
in_store_order = InStorePickupOrder()
in_store_order.process_order()

# Process a home delivery order
print("\nHome Delivery Order:")
home_delivery_order = HomeDeliveryOrder()
home_delivery_order.process_order()

# Process an international delivery order
print("\nInternational Delivery Order:")
international_order = InternationalDeliveryOrder()
international_order.process_order()

