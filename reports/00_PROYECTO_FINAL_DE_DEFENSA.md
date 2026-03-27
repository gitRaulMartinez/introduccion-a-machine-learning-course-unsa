# Informe Final de Proyecto y Defensa

## Analisis de Datos Oncologicos del Registro Institucional de Tumores de Argentina (RITA 2012-2022)

### Aplicacion de Tecnicas de Machine Learning No Supervisado

**Materia:** Introducción a Machine Learning  
**Universidad Nacional de Salta (UNSA)**

---

## Indice

1. [Introduccion y Contexto del Problema](#1-introduccion-y-contexto-del-problema)
2. [Descripcion del Dataset](#2-descripcion-del-dataset)
3. [Fase 1: Pre-procesado y Limpieza de Datos](#3-fase-1-pre-procesado-y-limpieza-de-datos)
4. [Fase 2: Analisis Exploratorio de Datos (EDA)](#4-fase-2-analisis-exploratorio-de-datos-eda)
5. [Fase 3: Aprendizaje No Supervisado (K-Modes)](#5-fase-3-aprendizaje-no-supervisado-k-modes)
6. [Fase 4: Experimentos con Diferentes Valores de K](#6-fase-4-experimentos-con-diferentes-valores-de-k)
7. [Fase 5: Sobre el Aprendizaje Supervisado - Limitaciones del Dataset](#7-fase-5-sobre-el-aprendizaje-supervisado---limitaciones-del-dataset)
8. [Conclusiones Generales](#8-conclusiones-generales)
9. [Referencias Tecnicas](#9-referencias-tecnicas)

---

## 1. Introduccion y Contexto del Problema

El cancer es una de las principales causas de mortalidad a nivel mundial. En Argentina, el Registro Institucional de Tumores de Argentina (RITA) recopila sistematicamente datos de diagnostico oncologico que abarcan informacion demografica (sexo, edad) y clinica (localizacion anatomica del tumor, tipo histologico de las celulas).

El objetivo de este proyecto es aplicar tecnicas de Machine Learning sobre el dataset RITA (periodo 2012-2022) para **descubrir patrones y perfiles ocultos** en la poblacion oncologica, utilizando un enfoque de aprendizaje **no supervisado** que permita segmentar a los pacientes en grupos con caracteristicas clinicas y demograficas similares.

### 1.1 Alcance del Proyecto

El proyecto sigue un flujo metodologico completo de ciencia de datos:

1. **Pre-procesado y limpieza** de los datos crudos.
2. **Analisis exploratorio** (EDA) para comprender distribuciones y relaciones.
3. **Aprendizaje no supervisado** con K-Modes para descubrir agrupamientos.
4. **Experimentacion con multiples valores de K** para evaluar la granularidad optima.
5. **Analisis critico** sobre la viabilidad del aprendizaje supervisado con este dataset.

### 1.2 Por que Machine Learning No Supervisado?

El dataset RITA no contiene una **variable objetivo natural** que permita formular un problema de prediccion supervisada (por ejemplo, no hay una columna de "resultado del tratamiento", "supervivencia" o "respuesta terapeutica"). Los datos registran el **diagnostico** del paciente, no su evolucion. Esto hace que el enfoque no supervisado sea el mas natural y util: descubrir estructura interna en los datos sin necesidad de etiquetas predefinidas.

---

## 2. Descripcion del Dataset

### 2.1 Origen y Dimensiones

- **Fuente:** Registro Institucional de Tumores de Argentina (RITA)
- **Periodo:** 2012 - 2022
- **Registros:** 82,106 pacientes
- **Columnas originales:** 13 variables
- **Archivo original:** `data/processed/rita-2012-2022.xlsx`

### 2.2 Variables Principales

| Variable | Tipo | Descripcion |
|----------|------|-------------|
| `IDPTE` | Identificador | Codigo unico del paciente |
| `PTESXN` | Categorica (2 niveles) | Sexo: Hombre / Mujer |
| `EDAD_DIAGNOSTICO` | Numerica continua | Edad al momento del diagnostico |
| `TOPOGRAFIA` / `TOPOGRAFIA_N` | Categorica (~600 niveles) | Localizacion anatomica del tumor (codificacion CIE-O-3) |
| `MORFOLOGIA` / `MORFOLOGIA_N` | Categorica (~600 niveles) | Tipo histologico de las celulas tumorales (codificacion CIE-O-3) |
| `FECHA_DIAGNOSTICO` | Fecha | Fecha del diagnostico |

### 2.3 Codificacion CIE-O-3 (Referencia)

**Topografias frecuentes:**

| Codigo | Organo | Notas Clinicas |
|--------|--------|----------------|
| C50.9 | Mama | Cancer mas frecuente en mujeres |
| C53.9 | Cuello uterino (cervix) | Asociado a VPH |
| C62.9 | Testiculo | Frecuente en hombres 15-45 años |
| C61.9 | Prostata | Predominante en hombres >65 años |
| C20.9 | Recto | Parte del cancer colorrectal |
| C34.9 | Pulmon | Asociado a tabaquismo |

**Morfologias frecuentes:**

| Codigo | Nombre | Significado |
|--------|--------|-------------|
| 8140 | Adenocarcinoma, SAI | Cancer en celulas glandulares. Tipo mas comun en general. |
| 8070 | Carcinoma escamoso | Cancer en celulas planas de revestimiento. Comun en cuello uterino y pulmon. |
| 8077 | NIC III (CIN III) | Lesion precancerosa de alto grado en cuello uterino. No es cancer invasivo aun. |
| 8500 | Carcinoma ductal infiltrante | Tipo mas comun de cancer de mama (70-80% de casos). Invasivo. |
| 8010 | Carcinoma, SAI | Clasificacion generica de cancer epitelial sin subtipo especificado. |

---

## 3. Fase 1: Pre-procesado y Limpieza de Datos

**Notebook:** `notebooks/01_preprocesado_limpieza.ipynb`

### 3.1 Limpieza de Nombres de Columnas

Los nombres originales de las columnas presentaban espacios en blanco al inicio y al final (ejemplo: `"PTESXN "` en lugar de `"PTESXN"`), lo cual dificultaba el acceso programatico. Se aplico una normalizacion masiva con `.str.strip()`.

### 3.2 Tratamiento de Valores Ausentes

| Variable | Valores Nulos | Porcentaje | Accion |
|----------|---------------|------------|--------|
| TOPOGRAFIA | 17 | 0.02% | Exclusion en modelado |
| MORFOLOGIA | 240 | 0.29% | Exclusion en modelado |
| Resto | 0 | 0% | Sin accion |

La fraccion de valores nulos es minima respecto al total de 82,106 registros. Se opto por la exclusion de estas filas durante el modelado para mantener la precision clinica, ya que imputar un tipo de tumor o localizacion anatomica careceria de sentido medico.

### 3.3 Deteccion de Outliers

Se aplico el metodo del **Rango Intercuartilico (IQR)** sobre la variable `EDAD_DIAGNOSTICO`:

- **Q1:** 44 años
- **Q3:** 66 años
- **IQR:** 22 años
- **Limite inferior:** 44 - 1.5 * 22 = 11 años
- **Limite superior:** 66 + 1.5 * 22 = 99 años

Se detecto 1 valor atipico extremo (edad > 100 años). Aunque es biologicamente posible, se identifico y registro para evitar que sesgara los promedios.

### 3.4 Recodificacion de Variables

- **Sexo:** Se creo la columna `SEXO_NUM` mapeando `Hombre -> 0` y `Mujer -> 1`.
- **Edad discretizada:** Se creo `EDAD_RANGO` con 4 categorias:
  - Infantil-Juvenil (0-18 años)
  - Adulto Joven (18-45 años)
  - Adulto (45-65 años)
  - Adulto Mayor (65+ años)

### 3.5 Dataset Generado

El proceso concluyo con la generacion de `data/processed/rita_limpio.csv`, que sirve como fuente unica para todas las etapas posteriores.

---

## 4. Fase 2: Analisis Exploratorio de Datos (EDA)

**Notebook:** `notebooks/02_eda_estadistica.ipynb`

### 4.1 Estadistica Descriptiva

| Metrica | Valor |
|---------|-------|
| Total de registros | 82,106 |
| Edad promedio | 55.08 años |
| Edad mediana | 57 años |
| Desviacion estandar | 15.45 años |
| Proporcion mujeres | 59.8% |
| Proporcion hombres | 40.2% |

### 4.2 Diferencias por Sexo

| Sexo | Edad Promedio | Mediana |
|------|---------------|---------|
| Hombres | 57.9 años | 60 años |
| Mujeres | 53.1 años | 54 años |

Las mujeres tienden a ser diagnosticadas a una edad mas temprana que los hombres, lo cual se explica por la alta incidencia del cancer de mama y las lesiones cervicales precancerosas (NIC III) que se detectan en edades tempranas mediante programas de screening.

### 4.3 Hallazgos Visuales

**Distribucion de Edad:**

![Distribucion de Edad](figures/01_histograma_edad.png)

*Figura 1: Distribucion de la edad de diagnostico. Se observa una distribucion asimetrica hacia la derecha con pico entre 55 y 65 años.*

**Matriz de Correlacion:**

![Matriz de Correlacion](figures/02_matriz_correlacion.png)

*Figura 2: Relaciones lineales entre variables numericas. No se encontraron correlaciones fuertes, lo que sugiere que las relaciones entre diagnostico y demografia son complejas y no lineales.*

### 4.4 Conclusiones del EDA

1. La poblacion oncologica tiene un sesgo hacia el sexo femenino (60/40), lo que debe considerarse en cualquier modelo.
2. La edad de diagnostico varia significativamente segun el organo afectado (40 años para ciertos tumores vs 70+ para otros).
3. La ausencia de correlaciones lineales fuertes indica que los modelos basados en arboles o clustering son mas apropiados que modelos lineales.

---

## 5. Fase 3: Aprendizaje No Supervisado (K-Modes)

**Notebook:** `notebooks/03_aprendizaje_no_supervisado.ipynb`

### 5.1 Por que K-Modes y no K-Means?

Esta es una decision tecnica fundamental del proyecto. Las variables principales del dataset (sexo, topografia del tumor, morfologia del tumor) son **categoricas**. El algoritmo K-Means:

- Calcula centroides como **promedios** (no tiene sentido promediar "Mama" con "Testiculo").
- Usa **distancia euclidiana** (carece de significado en datos categoricos).
- Requiere variables numericas continuas.

K-Modes resuelve estos problemas:

- Usa la **moda** (valor mas frecuente) como centroide de cada cluster.
- Mide la **disimilitud** como el numero de atributos que difieren entre dos registros (distancia de Hamming).
- Esta disenado especificamente para datos categoricos.

### 5.2 Variables Seleccionadas para el Clustering

| Variable | Justificacion |
|----------|---------------|
| PTESXN (Sexo) | Diferenciacion biologica fundamental en oncologia |
| TOPOGRAFIA_N | Localizacion anatomica del tumor (variable clinica principal) |
| MORFOLOGIA_N | Tipo histologico de las celulas (define tratamiento y pronostico) |
| EDAD_RANGO | Segmenta por etapa de vida (discretizada en 4 categorias) |

**Variables excluidas:** `IDPTE` (identificador sin valor predictivo), `FECHA_DIAGNOSTICO` (temporal, no relevante para perfiles).

### 5.3 Determinacion del K Optimo

Se aplico el **Metodo del Codo (Elbow Method)**: se entreno K-Modes para K=1 hasta K=10 y se grafico el costo total (suma de disimilitudes entre cada punto y la moda de su cluster).

![Curva de Elbow](figures/03_curva_elbow.png)

*Figura 3: Metodo del codo. El punto de inflexion se identifica en K=4, donde la reduccion del costo se estabiliza.*

### 5.4 Resultados del Modelo Base (K=4)

El modelo segmento a los 82,106 pacientes en 4 perfiles predominantes:

| Cluster | Sexo | Topografia | Morfologia | Edad | N (%) |
|---------|------|------------|------------|------|-------|
| **0** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto Mayor | 24,851 (30.3%) |
| **1** | Hombre | Testiculo (C62.9) | Adenocarcinoma (8140) | Adulto | 22,583 (27.5%) |
| **2** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto | 21,752 (26.5%) |
| **3** | Mujer | Cuello uterino (C53.9) | NIC III (8077) | Adulto Joven | 12,920 (15.7%) |

### 5.5 Interpretacion Clinica de los Clusters

- **Cluster 0 - Mujeres adultas mayores con cancer de mama:** El grupo mas numeroso. Refleja la alta incidencia del cancer de mama en mujeres mayores de 65 años, consistente con la epidemiologia conocida.

- **Cluster 1 - Hombres adultos (heterogeneo):** Agrupa toda la poblacion masculina adulta (45-65 años). Aunque la moda es testiculo, este cluster mezcla patologias diversas (testiculo, pulmon, colon, prostata). Es el cluster mas heterogeneo.

- **Cluster 2 - Mujeres adultas con cancer de mama:** Similar al cluster 0 pero en un rango de edad mas joven (45-65 años). Permite diferenciar perfiles epidemiologicos por edad dentro del mismo tipo de cancer.

- **Cluster 3 - Mujeres jovenes con lesiones cervicales precancerosas:** Mujeres de 18-45 años con NIC III (neoplasia intraepitelial cervical grado III). Este grupo es critico para politicas de prevencion temprana y programas de vacunacion contra VPH.

---

## 6. Fase 4: Experimentos con Diferentes Valores de K

**Notebooks:** `notebooks/05_experimentos_k_nosupervisado.ipynb` y `notebooks/06_experimentos_k5_k6_k7.ipynb`

El modelo base con K=4 captura los patrones mas gruesos de la poblacion oncologica. Para evaluar si existen subgrupos clinicamente relevantes ocultos, se realizaron experimentos sistematicos con K=4, 5, 6, 7 y 8.

### 6.1 Evolucion del Costo por Valor de K

| K | Costo | Reduccion vs. anterior |
|---|-------|------------------------|
| 4 | 150,855 | -- |
| 5 | 141,494 | -6.2% |
| 6 | 136,195 | -3.7% |
| 7 | 131,579 | -3.4% |

La reduccion del costo se **desacelera progresivamente**, lo cual es esperado: cada cluster adicional aporta menor ganancia en cohesion interna. El mayor salto ocurre de K=4 a K=5.

### 6.2 Descubrimientos por Incremento de K

#### K=5: Separacion de la patologia masculina por edad

El avance mas importante es la aparicion de un cluster dedicado al **cancer de prostata en adultos mayores** (100% hombres, 97.6% mayores de 65 años). Esto separa la patologia masculina en dos perfiles clinicamente distintos:

- **Cancer testicular** (hombres jovenes-adultos): tratamiento con cirugia + quimioterapia, alta tasa de curacion.
- **Cancer de prostata** (hombres >65 años): tratamiento con hormonoterapia + radioterapia, pronostico variable.

Esta distincion es clinicamente fundamental porque tienen perfiles de riesgo, tratamientos y pronosticos completamente diferentes.

#### K=6: Distincion de subtipos histologicos

Se logra una doble segmentacion:

1. **En mama:** Se separa el **Carcinoma Ductal Infiltrante (8500)** del Adenocarcinoma generico. El carcinoma ductal infiltrante es el subtipo mas comun y agresivo de cancer de mama (70-80% de los casos), con protocolos de tratamiento especificos.

2. **En cuello uterino:** Se separa la patologia cervical por gravedad: **NIC III precanceroso** en jovenes vs **cancer cervical invasivo** en adultas.

#### K=7: Cancer colorrectal como grupo emergente

Aparece un cluster dedicado al **cancer colorrectal masculino** (100% hombres, 95.9% adultos 45-65 años), con topografias de recto (21%) y colon (11.1%). Este es uno de los canceres mas frecuentes a nivel mundial y su aparicion como cluster separado confirma su relevancia epidemiologica.

### 6.3 Mapa de Perfiles Descubiertos por K

| Perfil Clinico | K=4 | K=5 | K=6 | K=7 |
|---------------|:---:|:---:|:---:|:---:|
| Mama, Adulto Mayor | Si | Si | Si | Si |
| Mama, Adulto | Si | Si | -- | -- |
| Mama, Carcinoma Ductal Infiltrante | -- | -- | Si | Si |
| Cuello uterino, NIC III, Adulto Joven | Si | Si | Si | Si |
| Cuello uterino, Adulto (invasivo) | -- | -- | Si | Si |
| Hombres, Testiculo, Adulto | Si | Si | Si | Si |
| Hombres, Prostata, Adulto Mayor | -- | Si | Si | Si |
| Hombres, Colorrectal, Adulto | -- | -- | -- | Si |

**Patron de descubrimiento:** Cada incremento de K revela un subgrupo que estaba "oculto" dentro de un cluster mas grande.

### 6.4 Cual es el Mejor K?

No existe un K "correcto" unico. La eleccion depende del **proposito** del analisis:

- **K=4 (resumen ejecutivo):** Suficiente para una vision general. Captura los 3 canceres mas frecuentes por sexo.
- **K=5 (politicas de salud publica):** Optimo para diferenciar perfiles por sexo y edad. La separacion prostata/testiculo es clinicamente imprescindible.
- **K=6 (planificacion hospitalaria):** Mejor relacion detalle/parsimonia. Distingue subtipos histologicos relevantes para tratamiento.
- **K=7 (investigacion epidemiologica):** Maxima granularidad sin fragmentacion. Incluye cancer colorrectal como perfil separado.

### 6.5 Visualizaciones de los Experimentos

Los experimentos generaron 3 tipos de visualizaciones para cada valor de K:

- **Perfiles radar:** Muestran la composicion de cada cluster en las 4 variables.
- **Descomposicion demografica:** Distribucion porcentual de sexo y edad en cada cluster.
- **Geometria de clusters:** Proyecciones PCA y t-SNE de los clusters en 2 dimensiones.

Estas visualizaciones se encuentran en `reports/k_experimentos/figures/`.

---

## 7. Fase 5: Sobre el Aprendizaje Supervisado - Limitaciones del Dataset

### 7.1 Que es el Aprendizaje Supervisado y que Requiere

El aprendizaje supervisado es una tecnica de Machine Learning donde un modelo aprende a predecir una **variable objetivo** (etiqueta) a partir de un conjunto de **variables de entrada** (features). Para que funcione se necesita:

1. **Una variable objetivo claramente definida** que represente un resultado o desenlace.
2. **Features independientes** que tengan poder predictivo real sobre esa variable objetivo.
3. **Suficiente variabilidad** en los datos para que el modelo pueda generalizar.

### 7.2 Por que NO se Puede Aplicar Aprendizaje Supervisado de Forma Significativa en este Dataset

El dataset RITA presenta una **limitacion estructural fundamental**: registra informacion del **diagnostico** del paciente, pero **no contiene datos sobre el resultado o desenlace** del mismo. Especificamente:

#### 7.2.1 Ausencia de Variable Objetivo Clinicamente Significativa

El dataset NO contiene:

- **Supervivencia** (si el paciente sobrevivio o no)
- **Respuesta al tratamiento** (remision, progresion, recaida)
- **Estadio del tumor** al momento del diagnostico (I, II, III, IV)
- **Tiempo de sobrevida** (meses/años desde el diagnostico)
- **Tipo de tratamiento recibido** (cirugia, quimioterapia, radioterapia)
- **Estado actual del paciente** (vivo, fallecido, en tratamiento)

Sin alguna de estas variables, **no hay un resultado que predecir**. Un modelo supervisado necesita aprender la relacion entre las entradas (caracteristicas del diagnostico) y una salida (resultado), pero aqui solo tenemos las entradas.

#### 7.2.2 El Problema de la Variable "Sexo" como Objetivo

En la tarea supervisada que se realizo como ejercicio academico, se utilizo el **sexo del paciente** como variable objetivo (predecir si el paciente es hombre o mujer a partir de su perfil diagnostico). Si bien se obtuvieron metricas aceptables (XGBoost con 78.4% de accuracy), este enfoque tiene limitaciones conceptuales importantes:

1. **Circularidad biologica:** La topografia del tumor (variable mas predictiva) esta directamente determinada por el sexo en muchos casos. Un tumor de prostata (C61.9) ocurre exclusivamente en hombres; un tumor de cuello uterino (C53.9) ocurre exclusivamente en mujeres. El modelo en realidad esta "memorizando" una relacion biologica obvia, no descubriendo un patron util.

2. **Utilidad practica nula:** Predecir el sexo de un paciente a partir de su diagnostico carece de valor clinico. El sexo ya se conoce al momento de registrar al paciente; no es una variable que necesite ser predicha.

3. **No es una pregunta de investigacion valida:** Las preguntas clinicamente relevantes serian "Dado este diagnostico, cual es la probabilidad de supervivencia?" o "Que tratamiento producira mejor resultado?", pero el dataset no tiene los datos para responderlas.

#### 7.2.3 Que Datos Harian Falta para un Modelo Supervisado Valido

Para poder aplicar aprendizaje supervisado con impacto clinico real, el dataset necesitaria incluir al menos:

| Variable Faltante | Ejemplo de Uso Supervisado |
|--------------------|---------------------------|
| Supervivencia (si/no) | Clasificacion de riesgo de mortalidad |
| Tiempo de sobrevida | Regresion de esperanza de vida post-diagnostico |
| Estadio TNM (I-IV) | Prediccion de estadio a partir de variables clinicas |
| Respuesta al tratamiento | Clasificacion de respuesta terapeutica |
| Recurrencia (si/no) | Prediccion de recaida |

### 7.3 Lo que SI se Logro: Valor del Enfoque No Supervisado

La ausencia de una variable objetivo no significa que el dataset carezca de valor analitico. El aprendizaje **no supervisado** es precisamente la herramienta adecuada para este tipo de datos porque:

1. **No requiere etiquetas:** Descubre estructura interna en los datos sin necesidad de un resultado predefinido.
2. **Genera conocimiento nuevo:** Los clusters identificados revelan patrones epidemiologicos que no eran evidentes a simple vista.
3. **Tiene aplicacion practica directa:**
   - **Politicas de salud publica:** Identificar grupos de riesgo para programas de prevencion (ej: cluster de NIC III en mujeres jovenes -> programa de vacunacion VPH).
   - **Planificacion hospitalaria:** Dimensionar recursos por perfil de paciente (ej: separar cancer de prostata de testiculo para asignar especialistas).
   - **Epidemiologia:** Entender la distribucion de canceres en la poblacion argentina.

### 7.4 Resumen Comparativo

| Aspecto | No Supervisado (K-Modes) | Supervisado (limitado) |
|---------|--------------------------|------------------------|
| Viabilidad con este dataset | Alta | Baja (sin variable objetivo real) |
| Resultado obtenido | 4-7 perfiles clinicos significativos | Prediccion de sexo (78.4%, pero trivial) |
| Valor clinico | Alto (segmentacion de riesgo) | Nulo (relacion circular) |
| Conclusion | Enfoque adecuado y principal del proyecto | Ejercicio academico, no aplicable clinicamente |

---

## 8. Conclusiones Generales

### 8.1 Logros del Proyecto

1. **Pre-procesamiento riguroso:** Se limpio y preparo un dataset de 82,106 registros oncologicos, tratando valores nulos, outliers y recodificando variables para su uso en algoritmos de ML.

2. **EDA completo:** Se identificaron las distribuciones clave, diferencias demograficas por sexo y la ausencia de correlaciones lineales, lo que oriento la seleccion de algoritmos.

3. **Segmentacion exitosa con K-Modes:** El modelo no supervisado logro identificar entre 4 y 7 perfiles clinicos de pacientes oncologicos, separando exitosamente:
   - Cancer de mama por rango de edad (adultas vs adultas mayores)
   - Cancer de mama por subtipo histologico (adenocarcinoma generico vs carcinoma ductal infiltrante)
   - Patologia masculina por edad (testiculo en jovenes vs prostata en mayores)
   - Lesiones cervicales precancerosas en mujeres jovenes
   - Cancer colorrectal masculino como grupo emergente

4. **Experimentacion sistematica:** Los experimentos con K=4 a K=7 demuestran que cada incremento de K descubre subgrupos clinicamente relevantes, con un patron claro de "descubrimiento progresivo" de perfiles.

5. **Analisis critico del supervisado:** Se identifico y documento la limitacion estructural del dataset para aprendizaje supervisado, explicando por que el enfoque no supervisado es el adecuado.

### 8.2 Limitaciones

1. **K-Modes es sensible a la inicializacion.** Se mitigo con `n_init=5`, pero corridas diferentes pueden producir asignaciones ligeramente distintas.

2. **Discretizacion de edad.** Reducir la edad a 4 rangos pierde informacion. Una alternativa seria K-Prototypes, que combina variables categoricas y numericas.

3. **Las modas representan solo el valor mas frecuente.** Un cluster con moda "Mama" puede incluir pacientes con otros tipos de cancer. Las distribuciones completas dentro de cada cluster dan una vision mas precisa.

4. **El metodo del codo es heuristico.** Metricas complementarias como el indice de silueta o Calinski-Harabasz podrian reforzar la seleccion de K.

### 8.3 Trabajo Futuro

- Obtener datos complementarios (supervivencia, estadio, tratamiento) para habilitar modelos supervisados con valor predictivo clinico.
- Explorar K-Prototypes para mantener la edad como variable continua.
- Aplicar analisis de asociacion dentro de cada cluster para descubrir patrones de co-ocurrencia.
- Expandir la experimentacion a K=8, K=9 y K=10 evaluando si se produce fragmentacion excesiva.

---

## 9. Referencias Tecnicas

### 9.1 Herramientas y Librerias

- **Python 3.x** como lenguaje de programacion.
- **Pandas** para manipulacion y analisis de datos.
- **Matplotlib / Seaborn** para visualizacion estadistica.
- **kmodes** (libreria Python) para el algoritmo K-Modes.
- **scikit-learn** para LabelEncoder, metricas y utilidades de ML.
- **SMOTE (imblearn)** para balanceo de clases (ejercicio supervisado).
- **XGBoost** para el modelo de clasificacion (ejercicio supervisado).

### 9.2 Estructura de Archivos del Proyecto

```
machine-learning/
├── data/
│   ├── raw/                          # Datos originales
│   └── processed/                    # Datos limpios
│       ├── rita_limpio.csv           # Dataset limpio (82,106 registros)
│       └── rita-2012-2022.xlsx    # Fuente original
├── notebooks/
│   ├── 01_preprocesado_limpieza.ipynb
│   ├── 02_eda_estadistica.ipynb
│   ├── 03_aprendizaje_no_supervisado.ipynb
│   ├── 04_aprendizaje_supervisado.ipynb
│   ├── 05_experimentos_k_nosupervisado.ipynb
│   └── 06_experimentos_k5_k6_k7.ipynb
├── reports/
│   ├── 00_PROYECTO_FINAL_DE_DEFENSA.md   # Este documento
│   ├── 01_reporte_procesado.md
│   ├── 02_reporte_eda.md
│   ├── 03_reporte_nosupervisado.md
│   ├── 04_reporte_supervisado.md
│   ├── RESULTADOS_ANALISIS.md
│   ├── figures/                          # Graficos principales
│   └── k_experimentos/                   # Experimentos con K
│       ├── REPORTE_K_EXPERIMENTOS.md
│       ├── figures/                      # 15 visualizaciones
│       └── rita_clusters_k{4-8}.csv      # Resultados por K
└── requirements.txt
```

### 9.3 Metodologia

El proyecto sigue la metodologia CRISP-DM (Cross-Industry Standard Process for Data Mining) adaptada al contexto academico:

1. **Comprension del negocio** -> Contexto oncologico y epidemiologico
2. **Comprension de los datos** -> EDA
3. **Preparacion de los datos** -> Pre-procesado y limpieza
4. **Modelado** -> K-Modes con experimentacion de K
5. **Evaluacion** -> Analisis de costos, perfiles y relevancia clinica
6. **Despliegue** -> Reportes y conclusiones

---

*Proyecto desarrollado para la materia de Introducción a Machine Learning - Universidad Nacional de Salta (UNSA)*
