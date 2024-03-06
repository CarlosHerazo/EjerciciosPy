"""
Consume la API de la NASA y extrae informacion crucial de los asteroides que pasan cerca de la tierra con sus dias

"""

import requests  # para hacer peticiones http o https
import json
from datetime import datetime, timedelta
from tabulate import tabulate


class NeoDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_dates(self):
        start_date = datetime.now().strftime("%Y-%m-%d")
        end_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        return start_date, end_date

    def get_build_api_url(self, start_date, end_date):
        base_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        print(base_url)
        return base_url

    def get_fetch_data(self, url):
        params = {"api_key": self.api_key}
        response = requests.get(url, params=params)
        return response

    def set_process_data(self, data):
        neo_data = data["near_earth_objects"]
        neo_table = []

        for date, neos in neo_data.items():
            for neo in neos:
                neo_info = {
                    "date": date,
                    "name": neo["name"],
                    "diameter_meters": neo["estimated_diameter"]["meters"][
                        "estimated_diameter_max"
                    ],
                    "distance_km": neo["close_approach_data"][0]["miss_distance"][
                        "kilometers"
                    ],
                }
                neo_table.append(neo_info)

        return neo_table

    def display_table(self, neo_table):
        headers = neo_table[0].keys()
        rows = [entry.values() for entry in neo_table]
        print(tabulate(rows, headers=headers, tablefmt="grid"))



api_key = "API_KEY"

neo_fetcher = NeoDataFetcher(api_key)

start_date, end_date = neo_fetcher.get_current_dates()
api_url = neo_fetcher.get_build_api_url(start_date, end_date)

response = neo_fetcher.get_fetch_data(api_url)

if response.status_code == 200:
    data = json.loads(response.text)
    neo_table = neo_fetcher.set_process_data(data)
    neo_fetcher.display_table(neo_table)
else:
    print(
        f"Error al realizar la solicitud. Codigo de estado: {response.status_code}"
    )
