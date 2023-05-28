from typing import Union

from package.temperature.Temperature import Temperature
from package.temperature.units.TemperatureUnit import TemperatureUnit
from package.temperature.validator import is_valid_unit


class TemperatureFactory:
    """Instanciate correct specific Temperature class"""

    @staticmethod
    def create(unit: TemperatureUnit, temperature: Union[int, float]):
        if not is_valid_unit(unit):
            raise Exception(f"Unknown '{unit}' temperature unit")
        return Temperature(unit, temperature)
