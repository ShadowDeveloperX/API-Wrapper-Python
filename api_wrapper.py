# api_wrapper.py
import requests
from config import API_KEY

class WeatherAPIWrapper:
    def __init__(self, api_key=API_KEY):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_weather_by_city(self, city_name):
        """
        Obtiene el clima de una ciudad especificada.
        """
        endpoint = f"{self.base_url}/weather"
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "No se pudo obtener el clima"}

    def get_forecast_by_city(self, city_name):
        """
        Obtiene el pronóstico de una ciudad especificada.
        """
        endpoint = f"{self.base_url}/forecast"
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "No se pudo obtener el pronóstico"}
