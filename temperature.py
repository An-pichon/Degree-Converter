from enum import Enum


class TemperatureUnit(Enum):
    CELCIUS = "celsius"
    FAHRENHEIT = "fahrenheit"


Temperatures = [
    TemperatureUnit.CELCIUS,
    TemperatureUnit.FAHRENHEIT,
]


class Temperature:
    """Represent a temperature"""

    def __init__(self, unit: TemperatureUnit, temperature: float):
        self.unit = unit
        self.temperature = temperature

    def to_farenheit(self):
        return Temperature(TemperatureUnit.FAHRENHEIT, self.temperature * 9 / 5 + 32)

    def to_celsius(self):
        return Temperature(TemperatureUnit.CELCIUS, (self.temperature - 32) * 5 / 9)

    def to_string(self):
        return f"{self.temperature}° {self.unit}"
