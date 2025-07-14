
#PORDUCT 

class VacationPackage:
    def __init__(self):
        self.destination = None
        self.accommodation = None
        self.transport = None
        self.activities = []
        self.meals = []

    def __str__(self):
        return (f"Vacation Package:\n"
                f"Destination: {self.destination}\n"
                f"Accommodation: {self.accommodation}\n"
                f"Transport: {self.transport}\n"
                f"Activities: {', '.join(self.activities) if self.activities else 'None'}\n"
                f"Meals: {', '.join(self.meals) if self.meals else 'None'}")


# Builder interface 
from abc import ABC, abstractmethod

class VacationBuilder(ABC):
    @abstractmethod
    def set_destination(self, destination): pass

    @abstractmethod
    def set_accommodation(self, accommodation): pass

    @abstractmethod
    def set_transport(self, transport): pass

    @abstractmethod
    def add_activity(self, activity): pass

    @abstractmethod
    def add_meal(self, meal): pass

    @abstractmethod
    def get_package(self): pass


# Concrete builder
class CustomVacationBuilder(VacationBuilder):
    def __init__(self):
        self.package = VacationPackage()

    def set_destination(self, destination):
        self.package.destination = destination
        return self

    def set_accommodation(self, accommodation):
        self.package.accommodation = accommodation
        return self

    def set_transport(self, transport):
        self.package.transport = transport
        return self

    def add_activity(self, activity):
        self.package.activities.append(activity)
        return self

    def add_meal(self, meal):
        self.package.meals.append(meal)
        return self

    def get_package(self):
        return self.package


#Director (Optional)

class VacationDirector:
    def __init__(self, builder: VacationBuilder):
        self.builder = builder

    def build_beach_vacation(self):
        return (self.builder
                .set_destination("Maldives")
                .set_accommodation("Beachfront Villa")
                .set_transport("Flight")
                .add_activity("Snorkeling")
                .add_activity("Sunbathing")
                .add_meal("Seafood Buffet")
                .get_package())

    def build_adventure_vacation(self):
        return (self.builder
                .set_destination("Swiss Alps")
                .set_accommodation("Mountain Cabin")
                .set_transport("Train")
                .add_activity("Skiing")
                .add_activity("Hiking")
                .add_meal("Hot Chocolate")
                .add_meal("Fondue")
                .get_package())

# Usage 

# Create a builder instance
builder = CustomVacationBuilder()

# Use the director to build predefined packages
director = VacationDirector(builder)

# Build a beach vacation package
beach_vacation = director.build_beach_vacation()
print(beach_vacation)

# Build a custom vacation by setting options manually
custom_vacation = (builder
                   .set_destination("Hawaii")
                   .set_accommodation("Resort")
                   .set_transport("Flight")
                   .add_activity("Surfing")
                   .add_activity("Volcano Tour")
                   .add_meal("Poke Bowl")
                   .get_package())

print(custom_vacation)
