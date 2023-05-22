#!/usr/bin/env python
# coding: utf-8
import PyInquirer

from converter import convert
from parser import parse_float
from temperature import Temperature, TemperatureUnit
from validator import is_float


def main():
    print("[ Degree Converter v0.1 ]")

    # Ask for source user inputs
    source_questions = [
        {
            'name': "unit",
            'message': "Which source temperature unit you want to convert?",
            'choices': [name for name in dir(TemperatureUnit) if not name.startswith('_')]
        },
        {
            'name': "temperature",
            'message': "Type a temperature number (in {source_unit}): ",
            'validate': lambda value: is_float(value),
        },
    ]
    source = PyInquirer.prompt(source_questions)

    # Ask for destination user inputs
    destination_questions = [
        {
            'name': "unit",
            'message': f"In which unit you want to convert {source_questions['temperature']}° {source_questions['unit']} to?",
            'choices': [name for name in dir(TemperatureUnit) if not name.startswith('_')]
        }
    ]
    destination = PyInquirer.prompt(destination_questions)

    # Instantiate the source temperature
    source_temperature = Temperature(source["unit"], parse_float(source["temperature"]))
    destination_temperature = convert(source_temperature, destination["unit"])

    print(
        f"{source_temperature.to_string()} in {destination_temperature.unit} is {destination_temperature.to_string()}"
    )


print([name for name in dir(TemperatureUnit) if not name.startswith('_')])

# main()
