import os

project_path = os.getcwd() + "/"
db_path = project_path + "data/clima.db"
api_endpoint = """https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&hourly=temperature_2m,precipitation&past_days=7&forecast_days=0"""

if __name__ == "__main__":
    from src.pipeline import pipeline
    pipeline = pipeline(db_path, api_endpoint)
    pipeline.run()