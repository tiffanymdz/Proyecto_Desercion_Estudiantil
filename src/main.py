#API PIP World Bank

from api.api import get_poverty_data

def main():
    data = get_poverty_data("CR", "SI.POV.DDAY")

    filtrado = []

    for item in data:
        year_str = item["year"]

        # Se verifica que el año no sea None o vacío
        if year_str is None or year_str.strip() == "":
            continue

        # Convertimos a entero
        year = int(year_str.strip())

        # Filtramos
        if 2020 <= year <= 2024:
            filtrado.append(item)

    for item in filtrado:
        print(f"{item['year']} → {item['value']}")


if __name__ == "__main__":
    main()
