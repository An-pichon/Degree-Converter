from typing import Union

from package.formulas import FahrenheitToCelsius, CelsiusToKelvin
from package.formulas.Formula import Formula


class FahrenheitToKelvin(Formula):
    """Represents a Fahrenheit to Kelvin mathematical formula"""

    def __init__(self):
        super().__init__()
        self._to_celsius = FahrenheitToCelsius()
        self._celsius_to_kelvin = CelsiusToKelvin()

    def _calculate(self, value: Union[int, float]) -> Union[int, float]:
        in_celsius = self._to_celsius.calculate(value)
        return self._celsius_to_kelvin.calculate(in_celsius)

    def _to_string(self) -> str:
        to_celsius = self._to_celsius.to_string()
        return self._celsius_to_kelvin.represent(to_celsius)
