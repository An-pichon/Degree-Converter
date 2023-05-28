#!/usr/bin/env python
# coding: utf-8

import PyInquirer
from colorama import Fore, Style

from package.temperature.factory.TemperatureFactory import TemperatureFactory
from package.temperature.parser import parse_float
from package.temperature.units.TemperatureUnit import TemperatureUnit
from package.temperature.validator import is_float

# Constants
VERSION = "2.0"


# Starts a conversion workflow
def convert():
    # 1. Ask for source user inputs
    source_temperature_unit = PyInquirer.prompt([
        {
            'type': "list",
            'name': "unit",
            'message': "Which source temperature unit do you want to convert?",
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
            'message': f"In which unit do you want to convert {source.to_string()} to?",
            'choices': [
                name for name in dir(TemperatureUnit) if
                not name.startswith('_')
                and TemperatureUnit[name] is not source_unit
            ]
        }
    ])['unit']
    destination_unit = TemperatureUnit[destination_temperature_unit]

    # 5. Convert the source temperature to destination unit
    source_destination_formula = source.get_formula_to(destination_unit)
    destination = source.to(unit=destination_unit)

    # 6. Print conversion formula & result!
    print(f"{Style.BRIGHT}")
    print(f"{Fore.GREEN}Input{Fore.RESET}       -> {Fore.GREEN}{source.to_string()}{Fore.RESET}")
    print()
    print(f"{Fore.RED}Destination{Fore.RESET} -> {Fore.RED}{destination_unit.value}{Fore.RESET}")
    print(f"{Fore.YELLOW}Formula{Fore.RESET}     -> {Fore.YELLOW}{source_destination_formula.to_string()}{Fore.RESET}")
    print(
        f"{' ' * len('Formula    ')} -> {Fore.YELLOW}{source_destination_formula.represent(source_temperature)}{Fore.RESET}"
    )
    print()
    print(f"{Fore.RED}Output{Fore.RESET}      -> {Fore.RED}{destination.to_string()}{Fore.RESET}")
    print(f"{Style.RESET_ALL}")


# Program logic
def main():
    print(f"[ Degree Converter v{VERSION} ]")
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
