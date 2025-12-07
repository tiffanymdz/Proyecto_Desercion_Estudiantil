# uso de API

import requests

BASE_URL = "https://api.worldbank.org/v2"

def get_poverty_data(country="CR", indicator="SI.POV.DDAY"):
    """
    Consulta datos de pobreza desde el API del Banco Mundial.
    country = código ISO del país (CR = Costa Rica, MX = México, etc)
    indicator = indicador de pobreza (SI.POV.DDAY = pobreza extrema $2.15)
    """

    url = f"{BASE_URL}/country/{country}/indicator/{indicator}?format=json"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error en el API: {response.status_code}")

    data = response.json()

    # El resultado viene en dos partes, en data[1] están los valores
    if data[1] is None:
        return []

    poverty_list = []

    for entry in data[1]:
        poverty_list.append({
            "year": entry["date"],
            "value": entry["value"]
        })

    return poverty_list