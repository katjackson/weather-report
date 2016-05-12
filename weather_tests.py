from weather_man import WeatherMan, CurrentWeather, TenDayWeather, SunPhase
import requests
import requests_mock
from weather import validate_location

""" testing regex validation """

# def test_validate_zip_location():
#     zip_valid = validate_location('27701')
#     assert zip_valid == ('27701', 'zip')
#
# def test_validate_abb_location():
#     abb_valid = validate_location('Atlantic Beach, NC')
#     print(abb_valid)
#     assert abb_valid == (('Atlantic Beach', 'NC'), 'abbreviation')
#
#
# def test_validate_full_location():
#     full_valid = validate_location('Greenville, North Carolina')
#     print(full_valid)
#     assert full_valid == (('Greenville', 'North Carolina'), 'full state')


""" WeatherMan tests """
# @requests_mock.Mocker()
# def test_function(m):
#     m.get('http://api.wunderground.com/api/c023973e2e852fc4/alerts/conditions/currenthurricane/forecast10day/astronomy/geolookup/q/27701.json', json={'a': 'b'})
#     return requests.get('http://api.wunderground.com/api/c023973e2e852fc4/alerts/conditions/currenthurricane/forecast10day/astronomy/geolookup/q/27701.json').json()
#
#
# @requests_mock.Mocker()
# def test_zip_init():
#     m.get('http://api.wunderground.com/api/c023973e2e852fc4/alerts/conditions/currenthurricane/forecast10day/astronomy/geolookup/q/27701.json', json={'a': 'b'})
#     wm = WeatherMan('27701')
#     assert wm.zip == '27701'
#
#
# def test_file_path():
#     wm = WeatherMan('27701')
#     assert wm.file_path == 'data/27701.json'
#
# def test_get_all_weather():
#     pass
#
# def test_get_location():
#     pass
#
# def get_full_location():
#     pass
