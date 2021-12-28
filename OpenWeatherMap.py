# OpenWeatherMap
import requests
import json
from datetime import datetime

class Owm_data():

    def __init__(self, api_key="your open weather map api key", lat="55.555555", lon="55.555555" ): # latitude, longitude    https://www.latlong.net
        
        self.api_key = api_key  
        self.lat = lat   
        self.lon = lon    
        self.url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
        self.response = requests.get(self.url)
        self.data = json.loads(self.response.text) 
          

    def get_temperature(self):
        return self.data["current"]["temp"]
        
    def get_pressure(self):
        return self.data["current"]["pressure"]

    def get_feels_like(self):
        return self.data["current"]["feels_like"]

    def get_humidity(self):
        return self.data["current"]["humidity"]

    def get_dew_point(self):
        return self.data["current"]["dew_point"]

    def get_wind_speed(self):
        return self.data["current"]["wind_speed"]

    def get_current_weather_main(self):
        return self.data["current"]["weather"][0]["main"]

    def get_current_weather_description(self):
        status = self.data["current"]["weather"][0]["description"]
        if status == "light rain":
            status = "Let regn"
        elif status == "scattered clouds":
            status = "Spredte skyer"
        elif status == "overcast clouds":
            status = "Overskyet"
        elif status == "broken clouds":
            status = "Pletvist overskyet"
        elif status == "moderate rain":
            status = "Moderat regn"
        elif status == "few clouds":
            status = "Få skyer"
        elif status == "mist":
            status = "Diset"
        elif status == "clear sky":
            status = "Skyfrit"
        elif status == "snow":
            status = "Sne"
        elif status == "fog":
            status = "Tåge"
        elif status == "light snow":
            stauts = "Let sne"
        return status

    def test(self):
        return self.data["current"]["weather"][0]["description"]

    def all_data(self):
        return self.data




vejr = Owm_data()
print(vejr.get_current_weather_description())


