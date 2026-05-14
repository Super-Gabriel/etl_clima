import sqlite3
import requests
import pandas as pd 


class Pipeline:
    def __init__(self, db_path:str, csv_path:str, api_endpoint:str):
        self.db_path = db_path
        self.csv_path = csv_path
        self.api_endpoint = api_endpoint

    def run(self):
        """metodo para ejecutar el ETL"""
        data = self.extract_data()
        df = self.transform_data(data)
        df.to_csv(self.csv_path, index=False)
        self.load_data()

    def extract_data(self) -> dict:
        """metodo para extraer los datos de la API"""
        try:
            response = requests.get(self.api_endpoint) # consulta a la API
            status_code = response.status_code # status code de la respuesta
            
            if status_code != 200: # verificando que el status code sea 200
                raise Exception(f"Error al extraer los datos: {status_code}")
            
            data = response.json() # convirtiendo la respuesta a json
            return data
        except Exception as e: # manejando errores de peticiones
            print(f"Error al extraer los datos: {e}")
            return None
    
    def transform_data(self, data:dict) -> pd.DataFrame:
        """metodo para transformar los datos"""
        try:
            hourly = data['hourly'] # los datos que interesan están en hourly
            df = pd.DataFrame(hourly)

            df['time'] = pd.to_datetime(df['time']) # transformando columna time a datetime
            df = df.rename(columns={# renombrando columnas
                'time': 'fecha',
                'temperature_2m': 'temperatura_c',
                'precipitation': 'precipitacion_mm'
            })

            #filtrando horas (solo de 6 am a 10 pm)
            df = df[(df['fecha'].dt.hour >= 6) & (df['fecha'].dt.hour <= 22)]

            numeric_cols = df.select_dtypes(include='number').columns # obteniendo columnas numericas
            mask = df[numeric_cols].isnull().any(axis=1) | (df[numeric_cols] < 0).any(axis=1) # verificando nulos o negativos en cualquier columna numerica
            nulos_o_negativos = df[mask]
            print(f"Cantidad de registros con valores nulos o negativos: {len(nulos_o_negativos)}")
            
            # si hay registros con valores nulos o negativos, se eliminan
            df = df.drop(nulos_o_negativos.index)
            
            return df
        except Exception as e:
            print(f"Error al transformar los datos: {e}")
            return None

    def load_data(self):
        """metodo para leer csv y subirlo a la base de datos"""
        try:
            df = pd.read_csv(self.csv_path) # leyendo csv
            conn = sqlite3.connect(self.db_path) # creando conexion
            df.to_sql('clima', conn, if_exists='replace', index=False) # cargando datos (se remplaza si existe)
            conn.close()
        except Exception as e:
            print(f"Error al cargar los datos: {e}")