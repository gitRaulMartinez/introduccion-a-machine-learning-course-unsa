# Configuración de Gemini CLI para este proyecto

## Instrucciones del Proyecto
- **Objetivo:** Análisis estadístico y Machine Learning sobre el dataset de salud "RITA".
- **Lenguaje:** Python 3.x.
- **Entorno:** Virtualenv `.venv` (activar con `source .venv/bin/activate`).
- **Frameworks:** Pandas, Scipy, Seaborn, Matplotlib, Openpyxl.

## Estado del Proyecto (Sesión 12/03/2026)

### 1. Hitos Logrados
- **Estructura Inicial:** Repositorio Git inicializado con carpetas estándar de ML (`data/`, `notebooks/`, `src/`, `models/`, `reports/`).
- **Pre-procesado:** Creado notebook `01_preprocesado_limpieza.ipynb`.
    - Limpieza de nombres de columnas.
    - Detección de outliers en `EDAD_DIAGNÓSTICO` (método IQR).
    - Recodificación de `PTESXN` (Sexo) a `SEXO_NUM` (0=H, 1=M).
    - Generación de dataset limpio: `data/processed/rita_limpio.csv`.
- **Análisis Exploratorio (EDA):** Creado notebook `02_eda_estadistica.ipynb`.
    - Resúmenes estadísticos y agrupaciones por sexo.
    - Visualizaciones: Histograma de edad, Proporción por sexo (Pie), Matriz de Correlación (Heatmap), Distribución de edad por Topografía (Boxplots).
- **Muestreo:** Generado `data/processed/rita_muestra_100.csv` con 100 registros aleatorios para pruebas rápidas.

### 2. Archivos Clave
- `data/processed/rita-2012-2022.xlsx`: Dataset original (Excel).
- `data/processed/rita_limpio.csv`: Dataset procesado completo.
- `data/processed/rita_muestra_100.csv`: Muestra reducida para otras fuentes.
- `notebooks/01_preprocesado_limpieza.ipynb`: Lógica de limpieza.
- `notebooks/02_eda_estadistica.ipynb`: Lógica de visualización y estadística.

### 3. Próximos Pasos (Pendiente)
- Iniciar la **Parte 3: Modelado de Machine Learning**.
- Definir la variable objetivo (Target) y las características (Features).
- Evaluar algoritmos de clasificación (ej: predecir sexo o tipo de tumor) o regresión (predecir edad).

## Registro de Prompts Importantes
- *Prompt de limpieza:* "Identifica y trata valores nulos y outliers en la columna edad usando IQR."
- *Prompt de EDA:* "Genera visualizaciones univariadas y multivariadas para entender la distribución de diagnósticos por sexo y topografía."
