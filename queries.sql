-- Consulta A: Temperatura promedio por día
-- Ordenada del día más caluroso al más frío
SELECT 
    DATE(fecha) AS dia,
    AVG(temperatura_c) AS temp_promedio
FROM clima
GROUP BY DATE(fecha)
ORDER BY temp_promedio DESC;


-- Consulta B: Horas con precipitación
-- Fechas y horas donde la precipitación fue mayor a 0 mm, ordenadas cronológicamente
SELECT 
    fecha,
    precipitacion_mm
FROM clima
WHERE precipitacion_mm > 0
ORDER BY fecha;


-- Consulta C: Día con mayor variación térmica
-- Día con la mayor diferencia entre temperatura máxima y mínima
SELECT 
    DATE(fecha) AS dia,
    (MAX(temperatura_c) - MIN(temperatura_c)) AS diff
FROM clima
GROUP BY DATE(fecha)
ORDER BY diff DESC
LIMIT 1;


-- Consulta D: Resumen diario
-- Temperatura mínima, máxima, promedio y precipitación total acumulada por día
SELECT 
    DATE(fecha) AS dia,
    MIN(temperatura_c) AS temp_min,
    MAX(temperatura_c) AS temp_max,
    AVG(temperatura_c) AS temp_promedio,
    SUM(precipitacion_mm) AS precipitacion_total
FROM clima
GROUP BY DATE(fecha);