from typing import Union

from package.temperature.Temperature import Temperature
from package.temperature.units.TemperatureUnit import TemperatureUnit


class TemperatureCelsius(Temperature):
    """A temperature represented as celsius degrees"""

    def __init__(self, temperature: Union[int, float]):
        super().__init__(unit=TemperatureUnit.CELSIUS, temperature=temperature)

    def to_fahrenheit(self):
        from package.temperature.factory.TemperatureFactory import TemperatureFactory
        return TemperatureFactory.create(unit=TemperatureUnit.FAHRENHEIT, temperature=self.temperature * 9 / 5 + 32)

    def to_celsius(self):
        return self

    def to_kelvin(self):
        from package.temperature.factory.TemperatureFactory import TemperatureFactory
        return TemperatureFactory.create(unit=TemperatureUnit.KELVIN, temperature=self.temperature + 273.15)
