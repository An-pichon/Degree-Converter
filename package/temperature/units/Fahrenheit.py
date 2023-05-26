from typing import Union

from package.temperature.Temperature import Temperature
from package.temperature.units.TemperatureUnit import TemperatureUnit


class TemperatureFahrenheit(Temperature):
    """A temperature represented as fahrenheit degrees"""

    def __init__(self, temperature: Union[int, float]):
        super().__init__(unit=TemperatureUnit.FAHRENHEIT, temperature=temperature)

    def to_fahrenheit(self):
        return self

    def to_celsius(self):
        from package.temperature.factory.TemperatureFactory import TemperatureFactory
        return TemperatureFactory.create(TemperatureUnit.CELSIUS, (self.temperature - 32) * 5 / 9)

    def to_kelvin(self):
        return self.to_celsius().to_kelvin()
