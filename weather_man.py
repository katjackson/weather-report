import os
import json
import requests

class WeatherMan:

    def __init__(self, zip_code):
        self.zip = zip_code
        self.file_path = "data/{}.json".format(zip_code)
        self.master_json = None
        self.city = None
        self.state = None
        self.get_all_weather()
        self.get_location()


    def get_all_weather(self):
        if not os.path.exists(self.file_path):
            # The following url is formatted with self.zip
            response = requests.get(
                """http://api.wunderground.com/api/c023973e2e852fc4/alerts/conditions/currenthurricane/forecast10day/astronomy/geolookup/q/{}.json""".format(self.zip)
                )
            response_json = response.json()

            with open(self.file_path, 'w') as f:
                    json.dump(response_json, f)

            self.master_json = response_json

        else:
            with open(self.file_path, 'r') as f:
                self.master_json = json.load(f)



    def get_location(self):
        self.city = self.master_json['location']['city']
        self.state = self.master_json['location']['state']

    def get_full_location(self):
        return "{}, {}".format(self.city, self.state)


class CurrentWeather(WeatherMan):

    def __init__(self, zip_code):
        super(CurrentWeather, self).__init__(zip_code)
        self.current = None
        self.weather = None
        self.temp = None
        self.feelslike = None
        self.get_current_conditions()

    def get_current_conditions(self):
        # high/low?
        self.current = self.master_json['current_observation']
        self.weather = self.current['weather']
        self.temp = self.current['temp_f']
        self.feelslike = self.current['feelslike_f']

    def __str__(self):
        return "Currently: {weather}\nTemp: {temp}°F \nFeels like: {feelslike}°F".format(
                    weather=self.weather,
                    temp=self.temp,
                    feelslike=self.feelslike
                    )


class TenDayWeather(WeatherMan):

    def __init__(self, zip_code):
        super(TenDayWeather, self).__init__(zip_code)
        self.ten_day = None
        self.get_ten_day()

    def get_ten_day(self):
        self.ten_day = self.master_json['forecast']['simpleforecast']['forecastday']

    def get_date(self, day_num):
        day = self.ten_day[day_num]
        dates = day['date']
        date = dates['weekday'] + " " + dates['monthname'] + " " + str(dates['day'])
        return date

    def __str__(self):
        day_strings = []
        day_print = "Date: {date}\nWeather: {conditions}\nHigh/Low: {high}°F / {low}°F\n"

        for day in range(10):
            day_weather = self.ten_day[day]

            date = self.get_date(day)
            conditions = day_weather['conditions']
            high = day_weather['high']['fahrenheit']
            low = day_weather['low']['fahrenheit']

            day_string = day_print.format(date=date, conditions=conditions,
                                          high=high, low=low)

            day_strings.append(day_string)
        return "\n".join(day_strings)


class SunPhase(WeatherMan):

    def __init__(self, zip_code):
        super(SunPhase, self).__init__(zip_code)
        self.sunrise_hour = None
        self.sunrise_min = None
        self.sunset_hour = None
        self.sunset_min = None
        self.get_sun_stuff()

    def get_sun_stuff(self):
        self.sunrise_hour = self.master_json['sun_phase']['sunrise']['hour']
        self.sunrise_min = self.master_json['sun_phase']['sunrise']['minute']
        self.sunset_hour = self.master_json['sun_phase']['sunset']['hour']
        self.sunset_min = self.master_json['sun_phase']['sunset']['minute']

    def sunrise(self):
        return str(int(self.sunrise_hour) % 12) + ":" + self.sunrise_min

    def sunset(self):
        return str(int(self.sunset_hour) % 12) + ":" + self.sunset_min

    def __str__(self):
        return "Sunrise: {} a.m.\nSunset: {} p.m.".format(self.sunrise(), self.sunset())


# class WeatherAlerts(WeatherMan):
#
#     def __init__(self, zip_code):
#         super(WeatherAlerts, self).__init__()
#         alerts =
#
