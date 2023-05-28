from package.temperature.units.TemperatureUnit import TemperatureUnit


def is_float(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_unit(unit) -> bool:
    return unit.name in dir(TemperatureUnit)
