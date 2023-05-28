from package.formulas.celsius.CelsiusToFahrenheit import CelsiusToFahrenheit
from package.formulas.celsius.CelsiusToKelvin import CelsiusToKelvin
from package.formulas.fahrenheit.FahrenheitToCelsius import FahrenheitToCelsius
from package.formulas.fahrenheit.FahrenheitToKelvin import FahrenheitToKelvin
from package.formulas.kelvin.KelvinToCelsius import KelvinToCelsius
from package.formulas.kelvin.KelvinToFahrenheit import KelvinToFahrenheit
from package.temperature.units.TemperatureUnit import TemperatureUnit


def get_temperature_formula_for_units(source: TemperatureUnit, destination: TemperatureUnit):
    if source is TemperatureUnit.CELSIUS:
        if destination is TemperatureUnit.KELVIN:
            return CelsiusToKelvin
        elif destination is TemperatureUnit.FAHRENHEIT:
            return CelsiusToFahrenheit
    elif source is TemperatureUnit.FAHRENHEIT:
        if destination is TemperatureUnit.CELSIUS:
            return FahrenheitToCelsius
        elif destination is TemperatureUnit.KELVIN:
            return FahrenheitToKelvin
    elif source is TemperatureUnit.KELVIN:
        if destination is TemperatureUnit.CELSIUS:
            return KelvinToCelsius
        elif destination is TemperatureUnit.FAHRENHEIT:
            return KelvinToFahrenheit
    else:
        raise Exception(f"Unknown formula for '{source.value}' to '{destination.value}' conversion")
