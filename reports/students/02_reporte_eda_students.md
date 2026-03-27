# Reporte EDA - Students (Columnas en Espanol)

## 1) Perfil general

- Dataset: `data/processed/students/students_limpio.csv`
- Dimensiones: **1194 x 31**
- Nulos totales: **2**

## 2) Hallazgos descriptivos principales

- Distribucion por `sexo`:
  - Male: 672
  - Female: 522
- Distribucion de `alguna_vez_probation`:
  - No: 896
  - Yes: 298
- `edad`:
  - Media: 21.34
  - Mediana: 21.0
  - Desviacion estandar: 1.61
- `cgpa_actual`:
  - Media: 3.17
  - Mediana: 3.21
  - Desviacion estandar: 0.75

## 3) Variables analizadas y que aporta cada una

- `edad`: permite observar etapa formativa y dispersion etaria.
- `sgpa_previo`: resume rendimiento reciente.
- `cgpa_actual`: resume rendimiento acumulado.
- `asistencia_promedio_clase`: aproxima compromiso academico.
- `horas_estudio_diario`: mide dedicacion diaria al estudio.
- `horas_redes_sociales_diario`: variable de posible distraccion.
- `sexo`: composicion poblacional.
- `alguna_vez_probation`: indicador de riesgo academico para modelado supervisado.

## 4) Que se obtuvo de cada bloque

- Bloque demografico (`sexo`, `edad`): cohorte predominantemente joven con leve mayoria masculina.
- Bloque rendimiento (`sgpa_previo`, `cgpa_actual`, `asistencia_promedio_clase`): senales directas del desempeno academico.
- Bloque habitos (`horas_estudio_diario`, `horas_redes_sociales_diario`, `modo_aprendizaje_preferido`): heterogeneidad de rutinas de aprendizaje.
- Bloque riesgo (`alguna_vez_probation`): desbalance moderado de clases, factor clave para definir estrategia de entrenamiento.

## 5) Visualizaciones generadas

- `reports/students/figures/01_histograma_edad_students.png`
- `reports/students/figures/02_histograma_cgpa_students.png`
- `reports/students/figures/03_matriz_correlacion_students.png`

## 6) Conclusion de EDA

El EDA confirma que la base es modelable y que el problema de riesgo academico requiere tecnicas de balanceo en supervisado para no favorecer excesivamente la clase mayoritaria (`No`).
