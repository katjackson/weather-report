import os
import re
import json
import requests
import argparse
from weather_man import WeatherMan, CurrentWeather, TenDayWeather, SunPhase

# current conditions √
# 10-day forecast √
# sunrise √
# sunset √
# current weather alerts
# all active hurricanes


def get_location_input():
    return input("Enter a zip code or city, state: ")

# regex validation for future use
def validate_location(location):
    if re.match(r'\d{5}', location):
        return location, 'zip'

    elif re.match(r'^(\w+\s*\w*)[,\s]+([A-Z]{2})$', location):
        city, state = re.match(r'^(\w+\s*\w*)[,\s]+([A-Z]{2})$',
                               location).groups()
        return (city, state), 'abbreviation'

    elif re.match(r'^(\w+\s*\w*)[,\s]+(\w+\s*\w*)$', location):
        city, state = re.match(r'^(\w+\s*\w*)[,\s]+(\w+\s*\w*)$',
                               location).groups()
        valid_by_input = input("Are you searching for {}, {}? y/N".format(
                                                                city, state))
        if valid_by_input.lower() != 'y':
            print("Please try entering your zip code.")
            get_location_input()
        return (city, state), 'full state'


def is_not_finished():
    response = input("Are you done here? Y/n\n")
    return response.lower() == 'n'


def main():
    if args.zip_code:
        zip_code = args.zip_code

    else:
        get_location_input()

    weather_man = WeatherMan(zip_code)
    current_weather = CurrentWeather(zip_code)
    ten_day_forecast = TenDayWeather(zip_code)
    sun_stuff = SunPhase(zip_code)

    print('\n')
    print("Today's Weather for {}".format(weather_man.get_full_location()))
    print('\n')
    print(current_weather)
    print(sun_stuff)
    print('\nTHIS IS THE 10-DAY FORECAST')
    print(ten_day_forecast)

    if is_not_finished():
            args.zip_code = None
            main()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Enter a zip code to view
                                        the weather for that location''')
    parser.add_argument('zip_code', type=str, help='lookup weather')
    args = parser.parse_args()
    main()
