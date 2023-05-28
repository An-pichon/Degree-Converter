from typing import Union

from package.formulas.Formula import Formula


class CelsiusToFahrenheit(Formula):
    """Represents a Celsius to Fahrenheit mathematical formula"""

    def _calculate(self, value: Union[int, float]) -> Union[int, float]:
        return value * 9 / 5 + 32

    def _to_string(self) -> str:
        return "{value} * 9 / 5 + 32"
