# INDICACIONES PARA REPLICAR EL PROYECTO CON OTRO DATASET

## Objetivo
Aplicar el mismo flujo de trabajo en un nuevo dataset, conservando el orden metodologico:
1) limpieza de datos, 2) EDA, 3) no supervisado, 4) supervisado.

## Flujo de tareas obligatorio

### 1. Limpieza y preprocesado
- Cargar datos originales desde `data/raw/`.
- Estandarizar nombres de columnas (quitar espacios, homogenizar formato).
- Revisar tipos de datos y corregir casteos necesarios.
- Detectar y tratar valores faltantes (imputacion o exclusion con justificacion).
- Detectar outliers en variables numericas (IQR/boxplot u otro metodo).
- Recodificar variables categoricas cuando el modelo lo requiera.
- Guardar dataset limpio en `data/processed/`.

### 2. EDA
- Obtener resumen del dataset (`shape`, `info`, `describe`).
- Analizar distribuciones de variables clave (histogramas, barras).
- Evaluar relaciones entre variables (correlacion, boxplots, cruces por grupos).
- Identificar patrones iniciales que orienten el modelado.
- Documentar hallazgos principales y posibles sesgos/desbalances.

### 3. Aprendizaje no supervisado
- Definir variables de entrada (idealmente categoricas para K-Modes).
- Codificar/transformar datos para el algoritmo elegido.
- Determinar numero optimo de clusters (metodo del codo u otro criterio).
- Entrenar modelo de clustering.
- Asignar cluster a cada registro.
- Interpretar centroides/modas y describir perfil de cada cluster.
- Reportar tamano de clusters y metrica de costo/cohesion.

### 4. Aprendizaje supervisado
- Definir variable objetivo y conjunto de features.
- Dividir train/test y aplicar validacion cruzada.
- Tratar desbalance de clases (SMOTE, class_weight, submuestreo, etc.).
- Entrenar al menos 2 modelos candidatos.
- Ajustar hiperparametros (GridSearchCV o RandomizedSearchCV).
- Comparar desempeno con metricas globales y por clase.
- Incluir matriz de confusion y reporte de clasificacion.
- Seleccionar modelo final con justificacion tecnica.

## Estructura recomendada del proyecto

- `data/raw/`: datos originales sin modificar.
- `data/processed/`: datos limpios y derivados.
- `notebooks/`:
  - `01_preprocesado_limpieza.ipynb`
  - `02_eda_estadistica.ipynb`
  - `03_aprendizaje_no_supervisado.ipynb`
  - `04_aprendizaje_supervisado.ipynb`
- `reports/`:
  - `01_reporte_procesado.md`
  - `02_reporte_eda.md`
  - `03_reporte_nosupervisado.md`
  - `04_reporte_supervisado.md`
  - `RESULTADOS_ANALISIS.md`
  - `00_PROYECTO_FINAL_DE_DEFENSA.md`
- `reports/figures/`: graficos exportados.
- `models/`: modelos entrenados y serializados.
- `src/`: utilidades o scripts reutilizables.

## Criterios minimos de calidad
- Trazabilidad: cada conclusion debe estar respaldada por una metrica o grafico.
- Reproducibilidad: pasos claros para volver a ejecutar todo el flujo.
- Coherencia: mismo criterio entre notebook, reporte y resultados finales.
- Interpretabilidad: explicar que significa cada resultado en terminos del problema.

## Entregables esperados
- Dataset limpio en `data/processed/`.
- 4 notebooks completos (limpieza, EDA, no supervisado, supervisado).
- Reportes markdown por fase y reporte final consolidado.
- Graficos clave en `reports/figures/`.
- Modelo final recomendado y justificado.
