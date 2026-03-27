# Resumen Detallado de Trabajo - Students (Columnas en Espanol)

## 1) Que se hizo

Se reestructuro todo el flujo de Students para trabajar con columnas en espanol y mantener total separacion respecto a RITA.

## 2) Estructura usada

- `data/raw/students/Students_Performance_dataset.csv`
- `data/processed/students/students_limpio.csv`
- `data/processed/students/students_clusterizado.csv`
- `data/processed/students/students_modelado.csv`
- `notebooks/students/`
- `reports/students/`
- `reports/students/figures/`
- `models/students/`

## 3) Traduccion de columnas (ejemplos)

- `gender` -> `sexo`
- `age` -> `edad`
- `what_was_your_previous_sgpa` -> `sgpa_previo`
- `what_is_your_current_cgpa` -> `cgpa_actual`
- `did_you_ever_fall_in_probation` -> `alguna_vez_probation`

## 4) Fase de limpieza

- Estandarizacion de nombres y limpieza de texto.
- Casteo de variables numericas.
- Control de calidad: 1194x31, 0 duplicados, 2 nulos, 13 outliers de edad (IQR).

## 5) Fase EDA

- Variables clave en espanol: `edad`, `sgpa_previo`, `cgpa_actual`, `asistencia_promedio_clase`, `horas_estudio_diario`, `horas_redes_sociales_diario`, `alguna_vez_probation`.
- Hallazgos: cohorte joven, desbalance de probation (No > Yes).
- Figuras: histogramas y matriz de correlacion en `reports/students/figures/`.

## 6) Fase no supervisada

- Algoritmo: K-Modes por naturaleza categorica de variables.
- Variables: `sexo`, `programa`, `modo_aprendizaje_preferido`, `nivel_ingles`, `habilidades_principales`, `area_interes`, `convivencia`, `alguna_vez_probation`.
- Seleccion K: codo con K=1..8, elegido **K=4** por interpretabilidad y utilidad.
- Salida: `students_clusterizado.csv`.

## 7) Fase supervisada

- Target: `alguna_vez_probation`.
- Motivo: es la etiqueta de riesgo academico util para alerta temprana.
- Modelos: Random Forest y XGBoost con balanceo SMOTE.
- Mejor modelo: XGBoost (F1 clase positiva 0.6154).

## 8) Notebooks actualizadas

- `notebooks/students/01_preprocesado_limpieza_students.ipynb`
- `notebooks/students/02_eda_estadistica_students.ipynb`
- `notebooks/students/03_aprendizaje_no_supervisado_students.ipynb`
- `notebooks/students/04_aprendizaje_supervisado_students.ipynb`

## 9) Resultado final

Todo el trabajo de Students quedo en espanol (columnas, notebooks y reportes), con trazabilidad completa y enfoque claro en interpretacion academica.
