from abc import ABC, abstractmethod
from typing import Union

from package.temperature.units.TemperatureUnit import TemperatureUnit


class Temperature(ABC):
    """Represent a temperature"""

    def __init__(self, unit: TemperatureUnit, temperature: Union[int, float]):
        self.unit = unit
        self.temperature = temperature
        super().__init__()

    @abstractmethod
    def to_fahrenheit(self): pass

    @abstractmethod
    def to_celsius(self): pass

    def to(self, unit: TemperatureUnit):
        return self.__getattribute__(f"to_{unit.value}")()

    def to_string(self):
        return f"{self.temperature}° {self.unit.value}"
