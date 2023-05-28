from typing import Union

from package.formulas import get_temperature_formula_for_units
from package.temperature.units.TemperatureUnit import TemperatureUnit


class Temperature:
    """Represent a temperature"""

    def __init__(self, unit: TemperatureUnit, temperature: Union[int, float]):
        self.unit = unit
        self.temperature = temperature
        super().__init__()

    def get_formula_to(self, unit: TemperatureUnit):
        return get_temperature_formula_for_units(self.unit, unit)()

    def to(self, unit: TemperatureUnit):
        formula = self.get_formula_to(unit)
        from package.temperature.factory.TemperatureFactory import TemperatureFactory
        return TemperatureFactory.create(unit, formula.calculate(value=self.temperature))

    @property
    def _temperature(self):
        # Temperature style
        return f"{self.temperature}°"

    @property
    def _unit(self):
        # Temperature style
        return self.unit.value

    def to_string(self):
        return f"{self._temperature} {self._unit}"
