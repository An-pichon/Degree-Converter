from temperature import Temperature, TemperatureUnit


def convert(temperature: Temperature, destination_unit: TemperatureUnit):
    # Convert to given destination temperature unit
    match destination_unit:
        case TemperatureUnit.CELCIUS:
            return temperature.to_celsius()
        case TemperatureUnit.FAHRENHEIT:
            return temperature.to_farenheit()
