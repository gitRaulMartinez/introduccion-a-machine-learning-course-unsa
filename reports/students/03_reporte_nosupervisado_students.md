# Reporte No Supervisado - Students (K-Modes, columnas en Espanol)

## 1) Objetivo

Segmentar perfiles de estudiantes sin etiqueta objetivo usando variables categoricas y el algoritmo K-Modes.

## 2) Variables usadas en clustering (espanol)

- `sexo`
- `programa`
- `modo_aprendizaje_preferido`
- `nivel_ingles`
- `habilidades_principales`
- `area_interes`
- `convivencia`
- `alguna_vez_probation`

Estas variables capturan contexto personal, academico y de habitos, con fuerte naturaleza categorica.

## 3) Por que K-Modes (y no K-Means)

- K-Means requiere variables numericas y trabaja con medias/distancias euclidianas.
- Aqui predominan categorias de texto (modo, habilidad, convivencia, etc.).
- K-Modes usa disimilitud por coincidencia y centroides tipo moda, por eso representa mejor el problema.

## 4) Seleccion de K y justificacion de K=4

Se evaluaron K=1..8 con metodo del codo (costo):

- 3439, 2867, 2641, 2456, 2236, 2241, 2179, 1992

Se adopto **K=4** por:

- equilibrio entre reduccion de costo y simplicidad interpretativa,
- mejor utilidad para intervencion academica (segmentos accionables),
- menor riesgo de sobre-fragmentacion frente a K mas altos.

Figura:

- `reports/students/figures/04_curva_elbow_students.png`

## 5) Resultado del modelo

- Costo final: **2438.0**
- Tamano de clusters:
  - Cluster 0: 388
  - Cluster 1: 443
  - Cluster 2: 200
  - Cluster 3: 163

Salida etiquetada:

- `data/processed/students/students_clusterizado.csv`

## 6) Interpretacion resumida de centroides

- Cluster 0: mayormente hombres, modo online, ingles intermedio, interes software, convivencia bachelor, probation no.
- Cluster 1: mayormente mujeres, modo offline, ingles intermedio, convivencia family, probation no.
- Cluster 2: mayormente hombres, modo offline, ingles intermedio, convivencia family, probation no.
- Cluster 3: mayormente hombres, modo offline, ingles basico, convivencia bachelor, probation no.

## 7) Que se obtuvo de esta fase

Se obtuvo una segmentacion interpretable para estrategias diferenciadas de acompanamiento segun perfil estudiantil (modo de aprendizaje, convivencia, nivel de ingles e historial academico).

## 8) Mejoras de visualizacion incorporadas

Para enriquecer la interpretacion de clusters, se agregaron tres vistas avanzadas:

### a) Geometria de clusters (PCA + t-SNE)

- Archivo: `reports/students/figures/06_cluster_geometry_students.png`
- Que muestra:
  - **PCA 2D**: proyeccion lineal global de separacion.
  - **t-SNE 2D**: estructura local no lineal entre observaciones.
- Utilidad: validar visualmente si los grupos forman regiones coherentes y diferenciadas en el espacio de caracteristicas.

### b) Radar de perfiles por cluster

- Archivo: `reports/students/figures/07_radar_profiles_students.png`
- Variables radar:
  - `cgpa_actual`
  - `horas_estudio_diario`
  - `asistencia_promedio_clase`
  - `puntaje_recursos`
  - `ratio_estudio_social`
  - `horas_productivas_totales`
  - `momentum_academico`
- Utilidad: comparar el "ADN conductual" de cada cluster sobre dimensiones academicas y de habitos.

### c) Composicion demografica por cluster

- Archivo: `reports/students/figures/08_demographic_breakdown_students.png`
- Que muestra:
  - distribucion de `sexo` por cluster,
  - distribucion de `convivencia` por cluster.
- Utilidad: entender como se reparte cada perfil en variables demograficas clave para decisiones de acompanamiento.

## 9) Variables derivadas agregadas para perfilado

Se incluyeron nuevas variables para analisis avanzado:

- `puntaje_recursos`: suma de acceso a smartphone y computadora personal.
- `ratio_estudio_social`: razon entre horas de estudio y horas en redes.
- `horas_productivas_totales`: estudio diario + desarrollo de habilidades.
- `momentum_academico`: diferencia `cgpa_actual - sgpa_previo`.

Estas variables no reemplazan el clustering original, sino que mejoran su explicacion e interpretabilidad.
