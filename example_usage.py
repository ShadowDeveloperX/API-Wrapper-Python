# examples/example_usage.py
from api_wrapper import WeatherAPIWrapper

# Crear instancia del wrapper
weather_api = WeatherAPIWrapper()

# Ejemplo de obtener el clima por ciudad
city = "Madrid"
weather = weather_api.get_weather_by_city(city)
print(f"Clima actual en {city}: {weather}")

# Ejemplo de obtener el pronóstico por ciudad
forecast = weather_api.get_forecast_by_city(city)
print(f"Pronóstico para {city}: {forecast}")
