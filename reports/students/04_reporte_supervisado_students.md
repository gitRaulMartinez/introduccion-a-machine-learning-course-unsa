# Reporte Supervisado - Students (Columnas en Espanol)

## 1) Objetivo del modelo

Predecir `alguna_vez_probation` (No=0, Yes=1), es decir, si el estudiante ha pasado por condicion academica de probation.

## 2) Por que se eligio esta variable objetivo

- Es una etiqueta institucional de riesgo academico directamente accionable.
- Permite disenar alertas tempranas para tutoria y acompanamiento.
- No existe en este dataset una etiqueta explicita de "aprobo/no aprobo examen final", por eso probation es el mejor objetivo disponible.

## 3) Variables predictoras consideradas

Se usan variables de cuatro bloques:

- Demograficas: `sexo`, `edad`.
- Academicas: `semestre_actual`, `asistencia_promedio_clase`, `sgpa_previo`, `cgpa_actual`, `creditos_completados`.
- Habitos y entorno: `horas_estudio_diario`, `horas_redes_sociales_diario`, `modo_aprendizaje_preferido`, `convivencia`.
- Contexto formativo: `nivel_ingles`, `tiene_beca_merito`, `habilidades_principales`, `area_interes`.

Razon: el riesgo de probation surge por combinacion de rendimiento, habitos y contexto.

## 4) Preparacion del entrenamiento

- Split estratificado train/test (`test_size=0.2`).
- Imputacion numerica (mediana) y categorica (moda).
- Codificacion OneHot para categoricas.
- Balanceo con SMOTE por desbalance de clases (`No`: 896, `Yes`: 298).

## 5) Modelos comparados

- Random Forest
- XGBoost

## 6) Metricas de test

### Random Forest
- Accuracy: 0.8033
- Precision (clase Yes): 0.7097
- Recall (clase Yes): 0.3667
- F1 (clase Yes): 0.4835

### XGBoost
- Accuracy: 0.8326
- Precision (clase Yes): 0.7273
- Recall (clase Yes): 0.5333
- F1 (clase Yes): 0.6154

## 7) Matriz de confusion del mejor modelo

Modelo seleccionado por F1 positivo: **XGBoost**.

- TN=167, FP=12
- FN=28, TP=32

Figura:

- `reports/students/figures/05_matriz_confusion_students.png`

## 8) Lectura tecnica y conclusion

- XGBoost mejora el equilibrio entre precision y recall en clase positiva (`Yes`), por eso supera a Random Forest.
- En este problema importa mas capturar casos en riesgo que solo maximizar accuracy global.
- Se recomienda XGBoost como modelo base de alerta academica.

Artefacto para modelado:

- `data/processed/students/students_modelado.csv`
