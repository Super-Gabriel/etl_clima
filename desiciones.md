# Decisiones Técnicas

## ¿Qué hace cada parte del pipeline?

El flujo inicia con el método `extract_data`, que realiza la llamada
a la API de Open-Meteo para obtener datos horarios de temperatura y
precipitación de los últimos 7 días para la CDMX. Los datos obtenidos
se pasan al método `transform_data`, que construye un DataFrame,
convierte la columna de fecha a tipo datetime, renombra las columnas
al español, filtra únicamente las horas entre las 06:00 y las 22:00,
e identifica registros con valores nulos o negativos. Finalmente,
`load_data` exporta el resultado limpio a un archivo CSV y lo carga
en una base de datos SQLite local.

## Decisiones técnicas importantes

- Se eligió una clase `Pipeline` para centralizar las rutas y
configuraciones como atributos, permitiendo que cualquier método
las consuma sin necesidad de pasarlas como parámetros en cada llamada.
Los métodos se separaron por responsabilidad para mantener el código
modular y que el método principal `run` sea fácil de leer de un vistazo.

- Para la verificación de la API se optó por una validación explícita
del código 200 en lugar de `raise_for_status()`, pensando en que a
futuro se podrían manejar otros códigos de respuesta de forma
diferenciada en ese mismo bloque.

- En la transformación, en lugar de filtrar nulos y negativos nombrando
explícitamente cada columna, se usó `select_dtypes(include='number')`
para detectar automáticamente todas las columnas numéricas, haciendo
el código más robusto ante posibles cambios en la estructura de datos.

## ¿Qué mejoraría con más tiempo?

- Usar variables de entorno para la URL y rutas en lugar de
  definirlas directamente en el código.
- Implementar pruebas unitarias para verificar la correctitud
  de cada método por separado.
- Agregar reintentos automáticos en `extract_data` en caso de
  fallo temporal de la API.