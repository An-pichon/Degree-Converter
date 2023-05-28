from typing import Union

from package.formulas.Formula import Formula


class FahrenheitToCelsius(Formula):
    """Represents a Fahrenheit to Celsius mathematical formula"""

    def _calculate(self, value: Union[int, float]):
        return (value - 32) * 5 / 9

    def _to_string(self) -> str:
        return "({value} - 32) * 5 / 9"
