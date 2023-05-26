from enum import Enum, unique


@unique
class TemperatureUnit(Enum):
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
    KELVIN = "kelvin"
