# API-Wrapper-Python

Este es un wrapper en Python para interactuar con la API de OpenWeather, permitiendo a los usuarios obtener datos sobre el clima actual y el pronóstico de una ciudad específica de manera sencilla y rápida.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

Este proyecto es un **API Wrapper** que facilita la interacción con la API de [OpenWeather](https://openweathermap.org/). Proporciona métodos para obtener el clima actual y el pronóstico meteorológico de cualquier ciudad mediante peticiones HTTP, manejando automáticamente los detalles de la configuración y los parámetros necesarios.

## Requisitos

- Python 3.x
- Librería Requests (`pip install requests`)

## Instalación

1. **Clona este repositorio**:

    ```bash
    git clone https://github.com/tu_usuario/API-Wrapper-Python.git
    cd API-Wrapper-Python
    ```

2. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

Antes de utilizar el wrapper, necesitas una **clave de API de OpenWeather**. Sigue estos pasos para configurarla:

1. Regístrate en [OpenWeather](https://home.openweathermap.org/users/sign_up) y obtén tu clave de API.
2. Abre el archivo `config.py` en el proyecto y agrega tu clave de API de la siguiente manera:

    ```python
    # config.py
    API_KEY = "tu_clave_de_openweather"
    ```

## Uso

Importa y utiliza la clase `WeatherAPIWrapper` para acceder a los datos climáticos.

```python
from api_wrapper import WeatherAPIWrapper

# Inicializa el wrapper
weather_api = WeatherAPIWrapper()

# Obtiene el clima actual de una ciudad
print(weather_api.get_weather_by_city("Madrid"))
