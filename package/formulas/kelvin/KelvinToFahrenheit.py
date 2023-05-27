from typing import Union

from package.formulas.Formula import Formula
from package.formulas.celsius.CelsiusToFahrenheit import CelsiusToFahrenheit
from package.formulas.kelvin.KelvinToCelsius import KelvinToCelsius


class KelvinToFahrenheit(Formula):
    """Represents a Kelvin to Fahrenheit mathematical formula"""

    def __init__(self):
        super().__init__()
        self._to_celsius = KelvinToCelsius()
        self._celsius_to_fahrenheit = CelsiusToFahrenheit()

    def _calculate(self, value: Union[int, float]) -> Union[int, float]:
        in_celsius = self._to_celsius.calculate(value)
        return self._celsius_to_fahrenheit.calculate(in_celsius)

    def _to_string(self) -> str:
        to_celsius = self._to_celsius.to_string()
        return self._celsius_to_fahrenheit.represent(to_celsius)
