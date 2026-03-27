# Proyecto de Estadística y Machine Learning

Este repositorio contiene la estructura base para un análisis estadístico y modelado de datos.

## Estructura del Proyecto

- `data/raw/`: datos originales.
- `data/processed/`: datos procesados.
- `notebooks/`: notebooks del proyecto.
- `reports/`: reportes y figuras.
- `models/`: modelos entrenados.
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
