# Step 1: Define the Base Interface (Coffee)

from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# Step 2: Implement the Basic Concrete Component (SimpleCoffee)

class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 5.0  # Base price for a simple coffee

    def get_description(self) -> str:
        return "Simple Coffee"


#Step 3: Create the Decorator Base Class

# We create an abstract CoffeeDecorator class that wraps around a Coffee object. All decorators will inherit from this class.

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost()

    def get_description(self) -> str:
        return self._coffee.get_description()


# Step 4: Implement Concrete Decorators

# MILK
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.5  # Add cost for milk

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"


# Sugar Decorator
class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5  # Add cost for sugar

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Sugar"


# Whipped Cream Decorator

class WhippedCreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 2.0  # Add cost for whipped cream

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Whipped Cream"


# Base coffee
coffee = SimpleCoffee()
print(f"{coffee.get_description()} - Cost: ${coffee.get_cost()}")

# Coffee with milk
coffee_with_milk = MilkDecorator(coffee)
print(f"{coffee_with_milk.get_description()} - Cost: ${coffee_with_milk.get_cost()}")

# Coffee with milk and sugar
coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print(f"{coffee_with_milk_sugar.get_description()} - Cost: ${coffee_with_milk_sugar.get_cost()}")

# Coffee with milk, sugar, and whipped cream
fancy_coffee = WhippedCreamDecorator(coffee_with_milk_sugar)
print(f"{fancy_coffee.get_description()} - Cost: ${fancy_coffee.get_cost()}")
