# etl_clima

Pipeline de extracción, transformación, carga y análisis de datos
climáticos de la Ciudad de México utilizando la API pública de Open-Meteo.

## Requisitos

- Python 3.8+
- Las dependencias están listadas en `requirements.txt` (pandas, requests
  y sus dependencias)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Super-Gabriel/etl_clima.git
   ```
   ```bash
   cd etl_clima
    ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo ejecutar

Desde la raíz del proyecto:
   ```bash
   python main.py
   ```

Esto generará automáticamente la carpeta `data/` con el archivo
`datos_clima_cdmx.csv` y la base de datos `clima.db`.

## Estructura del proyecto

```
etl_clima/
├── main.py
├── requirements.txt
├── queries.sql
├── decisiones.md
├── README.md
└── src/
    └── pipeline.py
```

## Consultas SQL

Las consultas de análisis se encuentran en `queries.sql`, diseñadas
para ejecutarse sobre la base de datos SQLite generada por el pipeline.