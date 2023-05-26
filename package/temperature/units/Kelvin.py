from typing import Union

from package.temperature.Temperature import Temperature
from package.temperature.units.TemperatureUnit import TemperatureUnit


class TemperatureKelvin(Temperature):
    """A temperature represented as kelvin degrees"""

    def __init__(self, temperature: Union[int, float]):
        super().__init__(unit=TemperatureUnit.KELVIN, temperature=temperature)

    def to_celsius(self):
        from package.temperature.factory.TemperatureFactory import TemperatureFactory
        return TemperatureFactory.create(unit=TemperatureUnit.CELSIUS, temperature=self.temperature - 273.15)

    def to_fahrenheit(self):
        return self.to_celsius().to_fahrenheit()

    def to_kelvin(self):
        return self
