import os

project_path = os.getcwd() + "/"
data_path = project_path + "data/"

db_path = data_path + "clima.db"
csv_path = data_path + "datos_clima_cdmx.csv"
api_endpoint = """https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&hourly=temperature_2m,precipitation&past_days=7&forecast_days=0"""

if __name__ == "__main__":
    os.makedirs(data_path, exist_ok=True) # creando directorio data si no existe
    from src.pipeline import Pipeline
    pipeline = Pipeline(db_path, csv_path, api_endpoint)
    pipeline.run()