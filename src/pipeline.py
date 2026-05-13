import sqlite3
import requests
import pandas as pd


class pipeline:
    def __init__(self, db_path, api_endpoint):
        self.db_path = db_path
        self.api_endpoint = api_endpoint

    def run(self):
        """metodo para ejecutar el ETL"""
        data = self.extract_data()
        print(data)


    def extract_data(self):
        """metodo para extraer los datos de la API"""
        try:
            response = requests.get(self.api_endpoint)
            status_code = response.status_code
            
            if status_code != 200:
                raise Exception(f"Error al extraer los datos: {status_code}")
            
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error al extraer los datos: {e}")
            return None
