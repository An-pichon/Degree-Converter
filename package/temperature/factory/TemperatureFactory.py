from typing import Union

from package.temperature.units.Celsius import TemperatureCelsius
from package.temperature.units.Fahrenheit import TemperatureFahrenheit
from package.temperature.units.Kelvin import TemperatureKelvin
from package.temperature.units.TemperatureUnit import TemperatureUnit


class TemperatureFactory:
    """Instanciate correct specific Temperature class"""

    @staticmethod
    def create(unit: TemperatureUnit, temperature: Union[int, float]):
        if unit is TemperatureUnit.CELSIUS:
            return TemperatureFactory._create_celsius(temperature)
        elif unit is TemperatureUnit.FAHRENHEIT:
            return TemperatureFactory._create_fahrenheit(temperature)
        elif unit is TemperatureUnit.KELVIN:
            return TemperatureFactory._create_kelvin(temperature)
        else:
            raise Exception(f"Unknown '{unit}' temperature unit")

    @staticmethod
    def _create_celsius(temperature: Union[int, float]):
        return TemperatureCelsius(temperature)

    @staticmethod
    def _create_fahrenheit(temperature: Union[int, float]):
        return TemperatureFahrenheit(temperature)

    @staticmethod
    def _create_kelvin(temperature: Union[int, float]):
        return TemperatureKelvin(temperature)
