from typing import Union

from package.formulas.Formula import Formula


class CelsiusToKelvin(Formula):
    """Represents a Celsius to Kelvin mathematical formula"""

    def _calculate(self, value: Union[int, float]):
        return value + 273.15

    def _to_string(self) -> str:
        return "{value} + 273.15"
