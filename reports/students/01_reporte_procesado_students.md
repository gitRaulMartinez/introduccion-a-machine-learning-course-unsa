# Reporte de Preprocesado y Limpieza - Students (Columnas en Espanol)

## 1) Fuente y separacion del proyecto

Se trabajo con:

- `data/raw/students/Students_Performance_dataset.csv` (fuente original)

Y se mantuvo separacion completa por dataset:

- `data/processed/students/`
- `notebooks/students/`
- `reports/students/`
- `models/students/`

## 2) Estandarizacion y traduccion de columnas

Primero se normalizaron los nombres a `snake_case` y luego se tradujeron al espanol tecnico para mejorar comprension.

Ejemplos:

- `gender` -> `sexo`
- `age` -> `edad`
- `current_semester` -> `semestre_actual`
- `what_was_your_previous_sgpa` -> `sgpa_previo`
- `what_is_your_current_cgpa` -> `cgpa_actual`
- `did_you_ever_fall_in_probation` -> `alguna_vez_probation`

## 3) Limpieza aplicada

- Recorte de espacios en variables de texto.
- Homogeneizacion de respuestas binarias `Yes/No`.
- Casteo numerico de variables clave (edad, SGPA, CGPA, asistencia, creditos, ingresos, etc.).
- Exportacion del dataset limpio final:
  - `data/processed/students/students_limpio.csv`

## 4) Control de calidad de datos

- Dimensiones: **1194 filas x 31 columnas**.
- Duplicados exactos: **0**.
- Nulos residuales: **2** en total.
- Outliers en `edad` (IQR): **13**.

## 5) Diccionario breve de variables clave (espanol)

- `sexo`: sexo del estudiante.
- `edad`: edad del estudiante.
- `programa`: carrera/programa academico.
- `semestre_actual`: avance curricular.
- `asistencia_promedio_clase`: compromiso academico por asistencia.
- `horas_estudio_diario`: habito de estudio.
- `horas_redes_sociales_diario`: exposicion a posible distractor.
- `sgpa_previo`: rendimiento inmediato anterior.
- `cgpa_actual`: rendimiento acumulado actual.
- `alguna_vez_probation`: historial de riesgo academico institucional.

## 6) Resultado de la fase

Se obtuvo una base consistente, con nombres comprensibles en espanol y lista para EDA, clustering y clasificacion sin ambiguedad semantica.
