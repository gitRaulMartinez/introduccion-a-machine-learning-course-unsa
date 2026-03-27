# Proyecto de Estadística y Machine Learning

Este repositorio contiene la estructura base para un análisis estadístico y modelado de datos.

## Estructura del Proyecto

- `data/raw/rita/` y `data/raw/students/`: datos originales por dataset.
- `data/processed/rita/` y `data/processed/students/`: datos procesados por dataset.
- `notebooks/rita/` y `notebooks/students/`: notebooks separados por proyecto.
- `reports/rita/` y `reports/students/`: reportes y figuras separados por proyecto.
- `models/rita/` y `models/students/`: modelos entrenados por dataset.
- `src/`: código fuente modular reutilizable.
- `GEMINI.md`: guía de prompts y mandatos para trabajar conmigo.

## Primeros Pasos Recomendados

1. **Dataset**: Coloca tu archivo de datos en `data/raw/`.
2. **Entorno**: Crea un entorno virtual e instala las dependencias necesarias.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. **Análisis Inicial**: Crea un notebook en `notebooks/` para cargar y explorar tus datos.
