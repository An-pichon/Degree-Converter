from abc import ABC, abstractmethod
from typing import Union

from colorama import Fore, Style

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

    @abstractmethod
    def to_kelvin(self): pass

    def to(self, unit: TemperatureUnit):
        return self.__getattribute__(f"to_{unit.value}")()

    @property
    def _temperature(self):
        # Temperature style
        return f"{Style.BRIGHT}{Fore.CYAN}{self.temperature}°{Fore.RESET}{Style.RESET_ALL}"

    @property
    def _unit(self):
        # Temperature style
        return f"{Style.BRIGHT}{Fore.MAGENTA}{self.unit.value}{Fore.RESET}{Style.RESET_ALL}"

    def to_string(self):
        return f"{self._temperature} {self._unit}"
