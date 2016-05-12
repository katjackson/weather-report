# Weather Report Program
This program takes in a zip code, sends a request to the Weather Underground API, displays a a weather report.

### Command Line
This program can be run from the command line by following the file call with a valid zip code.

## WeatherMan
The weather_man.py file contains the WeatherMan class. When instantiated, the WeatherMan class searches for a cached json of the requested data, and if the file does not exist, it queries the Weather Underground API and saves the response as a json.
*__str__*
The WeatherMan and its subclasses have string functions for printing out the attributes in an accessible way.

## WeatherMan subclasses
### CurrentWeather
After following the WeatherMan init, the CurrentWeather class creates attributes
for the current conditions and temperature.

### TenDayWeather
After following the WeatherMan init, the TenDayWeather class creates attributes for the ten day forecast and the string function extracts and prints the relevant data.

### SunPhase
After following the WeatherMan init, the SunPhase class creates attributes for the sunset and sunrise times.
