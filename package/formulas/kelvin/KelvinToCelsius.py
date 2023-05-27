from typing import Union

from package.formulas.Formula import Formula


class KelvinToCelsius(Formula):

    def _calculate(self, value: Union[int, float]) -> Union[int, float]:
        return value - 273.15

    def _to_string(self) -> str:
        return "{value} - 273.15"
