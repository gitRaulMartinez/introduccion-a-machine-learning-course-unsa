Objetivo General de la Tarea: Realizar el proceso de transformación de los datos en bruto para asegurar su calidad y fiabilidad, seguido de un análisis exploratorio que permita comprender la estructura, distribución y relación de las variables. Esto sentará las bases necesarias para la posterior aplicación de modelos de Machine Learning (supervisados y no supervisados)
.

--------------------------------------------------------------------------------
Parte 1: Pre-procesado, limpieza y recodificación El objetivo de esta fase es limpiar y dar formato al conjunto de datos mediante las siguientes acciones
:
Identificación y tratamiento de valores ausentes (Missing values): Buscar celdas vacías o nulas en las observaciones y decidir la acción a tomar, ya sea excluyendo (eliminando filas/columnas) o imputando y reemplazando los datos por un valor representativo, como el promedio
.
Detección de datos atípicos (Outliers): Identificar las observaciones extremadamente alejadas del resto, ya que su presencia puede afectar gravemente la fiabilidad de las técnicas de minería de datos que se aplicarán después
.
Operaciones de manipulación (CRUD): Modificar celdas de forma masiva (por ejemplo, usando apply y lambda), renombrar columnas mediante diccionarios, y agregar o eliminar características/filas para adecuar la estructura del DataFrame
.
Recodificación y casteo: Cambiar los tipos de datos cuando sea necesario (por ejemplo, formatear una matriz con pd.DataFrame) y recodificar valores categóricos a numéricos para facilitar su procesamiento por los algoritmos
.
Parte 2: Análisis Exploratorio de Datos (EDA) El objetivo de esta fase es extraer conocimiento inicial, tendencias y patrones utilizando herramientas de estadística descriptiva y visualización, con librerías como Pandas, Matplotlib y Seaborn
:
Resúmenes Estadísticos: Emplear operadores de resumen como describe() e info() para entender las dimensiones, mínimos, máximos, promedios y frecuencias (valores únicos) de las columnas
.
Agrupamiento de información: Utilizar métodos como groupby() para agregar y resumir datos estadísticos condicionados a diferentes categorías
.
Análisis Gráfico Univariado y Multivariado:
Histogramas: Mostrar la distribución de los datos numéricos y analizar si siguen una distribución normal
.
Gráficos de Dispersión (Scatterplots): Evaluar si existe una relación (lineal o no lineal) y nubes de puntos entre diferentes variables
.
Boxplots: Detectar visualmente la asimetría en la distribución de las variables e identificar posibles cuartiles y outliers
.
Gráficos de Torta: Representar la proporción de las categorías presentes en el dataset
.
Matriz de Correlación (Mapas de calor / Heatmaps): Medir matemáticamente e ilustrar la relación lineal entre variables numéricas continuas para descartar o confirmar correlaciones fuertes o despreciables
.
Coordenadas Paralelas: Visualizar cómo la variable categórica interactúa con múltiples dimensiones numéricas en paralelo
.