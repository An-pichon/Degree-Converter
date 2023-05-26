#!/usr/bin/env python
# coding: utf-8

import PyInquirer
from colorama import Fore, Style

from package.temperature.factory.TemperatureFactory import TemperatureFactory
from package.temperature.parser import parse_float
from package.temperature.units.TemperatureUnit import TemperatureUnit
from package.temperature.validator import is_float


def convert():
    # 1. Ask for source user inputs
    source_temperature_unit = PyInquirer.prompt([
        {
            'type': "list",
            'name': "unit",
            'message': "Which source temperature unit you want to convert?",
            'choices': [name for name in dir(TemperatureUnit) if not name.startswith('_')]
        }
    ])['unit']
    source_unit = TemperatureUnit[source_temperature_unit]

    # 2. Ask for source unit temperature value
    source_temperature = PyInquirer.prompt([{
        'type': 'input',
        'name': "temperature",
        'message': f"Type a temperature number (in {source_unit.value}): ",
        'validate': lambda value: is_float(value),
    }])['temperature']

    # 3. Instantiate the source temperature
    source = TemperatureFactory.create(unit=source_unit, temperature=parse_float(source_temperature))

    # 4. Ask for destination user inputs
    destination_temperature_unit = PyInquirer.prompt([
        {
            'type': "list",
            'name': "unit",
            'message': f"In which unit you want to convert {source_temperature}° {source_unit.value} to?",
            'choices': [
                name for name in dir(TemperatureUnit) if
                not name.startswith('_')
                and TemperatureUnit[name] is not source_unit
            ]
        }
    ])['unit']
    destination_unit = TemperatureUnit[destination_temperature_unit]

    # 5. Convert the source temperature to destination unit
    destination = source.to(unit=destination_unit)

    # 6. Print converted temperature!
    print(
        f"{source.to_string()} {Style.BRIGHT}{Fore.YELLOW}",
        "<{{===}}>"
        f"{Fore.RESET}{Style.RESET_ALL} {destination.to_string()}"
    )


def main():
    print("[ Degree Converter v0.1 ]")
    again = True

    while again:
        convert()
        again = PyInquirer.prompt([{
            'type': 'confirm',
            'name': 'again',
            'message': 'Another conversion?',
        }])['again']

    print(f"Thank you, good bye! :)")


if __name__ == '__main__':
    main()
