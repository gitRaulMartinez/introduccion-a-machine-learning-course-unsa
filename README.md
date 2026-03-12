# Proyecto de Estadística y Machine Learning

Este repositorio contiene la estructura base para un análisis estadístico y modelado de datos.

## Estructura del Proyecto

- `data/`: Datos crudos (`raw/`) y procesados (`processed/`).
- `notebooks/`: Análisis exploratorio de datos (EDA) y experimentos iniciales.
- `src/`: Código fuente modular (limpieza de datos, funciones estadísticas, etc.).
- `models/`: Archivos de modelos entrenados (ej: .pkl, .h5).
- `reports/`: Resultados del análisis y visualizaciones (`figures/`).
- `GEMINI.md`: Guía de prompts y mandatos para trabajar conmigo.

## Primeros Pasos Recomendados

1. **Dataset**: Coloca tu archivo de datos en `data/raw/`.
2. **Entorno**: Crea un entorno virtual e instala las dependencias necesarias.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. **Análisis Inicial**: Crea un notebook en `notebooks/` para cargar y explorar tus datos.
