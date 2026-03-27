# Reporte de Análisis Exploratorio de Datos (EDA)

Este reporte presenta los hallazgos iniciales, tendencias y patrones identificados en el dataset de registros oncológicos "RITA" tras el proceso de limpieza.

## 1. Resúmenes Estadísticos (describe / info)

### 1.1 Perfil General del Dataset
- **Dimensiones:** El dataset analizado cuenta con 82,106 registros y 13 columnas.
- **Variable Edad:**
    - Promedio: 55.08 años.
    - Mediana: 57 años.
    - Desviación Estándar: 15.45 años.
- **Distribución por Sexo:** Aproximadamente el 59.8% de los registros corresponden a mujeres y el 40.2% a hombres.

### 1.2 Agrupamiento de Información (groupby)
Al analizar la edad promedio de diagnóstico por sexo, se observan diferencias notables:
- **Hombres:** Edad promedio de 57.9 años (Mediana: 60).
- **Mujeres:** Edad promedio de 53.1 años (Mediana: 54).
- **Conclusión:** Las mujeres en este dataset tienden a ser diagnosticadas a una edad ligeramente más temprana que los hombres.

## 2. Análisis Visual (Seaborn / Matplotlib)

### 2.1 Análisis Univariado
- **Histogramas de Edad:** Se observa una distribución asimétrica hacia la derecha, con un pico de diagnósticos entre los 55 y 65 años.
- **Gráficos de Torta:** Confirman visualmente la mayor proporción de pacientes de sexo femenino en los registros.

### 2.2 Análisis Multivariado
- **Matriz de Correlación (Heatmap):** No se encontraron correlaciones lineales fuertes entre las variables numéricas codificadas (ej. edad vs comportamiento), lo cual sugiere que la relación entre diagnóstico y demografía es más compleja y requiere modelos no lineales.
- **Boxplots (Edad por Topografía):** Se identificaron diferencias significativas en la edad de diagnóstico según el órgano afectado. Por ejemplo, ciertos tumores tienen una mediana de edad cercana a los 40 años, mientras que otros superan los 70 años.

## 3. Conclusión Estratégica
Los datos están listos para la aplicación de modelos. La disparidad en la frecuencia de sexos sugiere que se debe tener cuidado con el desbalanceo de clases en los modelos supervisados.
