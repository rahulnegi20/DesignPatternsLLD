"""
In this example:

    We define a WeatherStation as the subject, which holds weather data.
    We create an Observer interface with a update method for observers.
    We implement specific observers like TemperatureDisplay, HumidityDisplay, and ForecastDisplay, which update themselves based on changes in WeatherStation.
"""

# Step 1: Define the Observer Interface

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass



# Step 2: Create Concrete Observers

class TemperatureDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Temperature Display: Current temperature is {temperature}°C")

class HumidityDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Humidity Display: Current humidity is {humidity}%")

class ForecastDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Forecast Display: Atmospheric pressure is {pressure} hPa")


# Step 3: Define the Subject (WeatherStation)

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_weather_data(self, temperature: float, humidity: float, pressure: float) -> None:
        print("\nWeatherStation: Weather data updated.")
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


# USage

# Create the WeatherStation (subject)
weather_station = WeatherStation()

# Create displays (observers)
temp_display = TemperatureDisplay()
humidity_display = HumidityDisplay()
forecast_display = ForecastDisplay()

# Register observers with the WeatherStation
weather_station.add_observer(temp_display)
weather_station.add_observer(humidity_display)
weather_station.add_observer(forecast_display)

# Simulate a weather data update
weather_station.set_weather_data(temperature=25.5, humidity=65, pressure=1013)
weather_station.set_weather_data(temperature=28.2, humidity=70, pressure=1012)
