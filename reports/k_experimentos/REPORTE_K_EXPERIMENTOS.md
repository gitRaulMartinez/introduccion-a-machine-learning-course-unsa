# Reporte de Experimentacion con Valores de K (K-Modes) - Dataset RITA

## 1. Introduccion y Objetivo

Este reporte documenta los resultados de la experimentacion con diferentes valores de K (4, 5, 6 y 7) en el algoritmo **K-Modes** aplicado al dataset RITA de registros oncologicos. El objetivo es evaluar si al incrementar el numero de clusteres se descubren **subgrupos clinicamente relevantes** que el modelo base (K=4) no logra capturar.

### 1.1 Contexto del Algoritmo

Se utiliza **K-Modes** en lugar de K-Means porque las variables del dataset son predominantemente **categoricas** (sexo, topografia del tumor, morfologia del tumor, rango de edad). K-Modes mide la **disimilitud** entre observaciones contando cuantos atributos difieren entre dos registros, en vez de calcular distancias euclidianas (que carecen de sentido en datos categoricos).

### 1.2 Variables Utilizadas

| Variable | Tipo | Descripcion |
|----------|------|-------------|
| **PTESXN** | Categorica (2 niveles) | Sexo del paciente: Hombre / Mujer |
| **TOPOGRAFIA_N** | Categorica (~600 niveles) | Localizacion anatomica del tumor segun codificacion CIE-O-3 (ej. C50.9 = Mama, C62.9 = Testiculo) |
| **MORFOLOGIA_N** | Categorica (~600 niveles) | Tipo histologico de las celulas tumorales segun CIE-O-3 (ej. 8140 = Adenocarcinoma, 8070 = Carcinoma escamoso) |
| **EDAD_RANGO** | Categorica (4 niveles) | Edad discretizada: Infantil-Juvenil (0-18), Adulto Joven (18-45), Adulto (45-65), Adulto Mayor (65+) |

### 1.3 Glosario de Morfologias (Tipos Histologicos)

Para la correcta interpretacion de los resultados, es fundamental entender que significa cada tipo morfologico:

| Codigo | Nombre | Significado Clinico |
|--------|--------|---------------------|
| **8140** | **Adenocarcinoma, SAI** | Cancer que se origina en celulas glandulares (que producen secreciones). Es el tipo mas comun de cancer en general. Aparece en mama, prostata, pulmon, colon, estomago, etc. "SAI" significa "Sin Otra Indicacion", es decir, es una clasificacion generica. |
| **8070** | **Carcinoma escamoso (epidermoide)** | Cancer que se origina en celulas escamosas (celulas planas que recubren superficies). Es comun en cuello uterino, pulmon, piel, laringe y esofago. Se asocia frecuentemente con factores como el VPH (en cuello uterino) o el tabaquismo (en pulmon/laringe). |
| **8077** | **Neoplasia intraepitelial cervical grado III (NIC III / CIN III)** | Lesion precancerosa de alto grado en el cuello uterino. No es cancer invasivo todavia, pero tiene alto riesgo de progresion. Se detecta mediante citologia (Papanicolaou) y esta fuertemente asociada a infeccion por VPH. Es la lesion mas grave antes de convertirse en carcinoma invasivo. |
| **8500** | **Carcinoma ductal infiltrante, SAI** | Es el tipo mas comun de cancer de mama (70-80% de los casos). Se origina en los ductos mamarios (conductos de la leche) y ha penetrado la pared del ducto invadiendo el tejido circundante ("infiltrante" = invasivo). |
| **8010** | **Carcinoma, SAI** | Clasificacion generica de cancer epitelial cuando no se ha determinado el subtipo especifico. Indica que se confirmo malignidad pero sin especificar si es escamoso, glandular u otro. |

### 1.4 Glosario de Topografias (Localizaciones Anatomicas)

| Codigo CIE-O | Organo | Notas Clinicas |
|---------------|--------|----------------|
| **C50.9** | Mama, SAI | Cancer de mama sin especificar ubicacion exacta dentro de la mama |
| **C50.4** | Cuadrante superior externo de la mama | Localizacion mas frecuente del cancer de mama (50% de los casos) |
| **C53.9** | Cuello uterino (cervix) | Cancer cervical, asociado a VPH |
| **C62.9** | Testiculo, SAI | Cancer testicular, mas frecuente en hombres de 15-45 anos |
| **C61.9** | Prostata, SAI | Cancer de prostata, predominante en hombres >65 anos |
| **C20.9** | Recto, SAI | Cancer rectal (parte del cancer colorrectal) |
| **C18.9** | Colon, SAI | Cancer de colon (parte del cancer colorrectal) |
| **C34.9** | Pulmon, SAI | Cancer de pulmon, asociado a tabaquismo |
| **C64.9** | Rinon, SAI | Cancer renal |
| **C42.1** | Medula osea | Leucemias y neoplasias hematologicas |
| **C54.1** | Endometrio | Cancer de cuerpo uterino |
| **C32.9** | Laringe, SAI | Cancer de laringe, asociado a tabaquismo |

---

## 2. Configuracion Experimental

- **Dataset:** `data/processed/rita_limpio.csv`
- **Filas utilizadas:** 82,106 registros de pacientes
- **Algoritmo:** K-Modes con `init='random'`, `n_init=5`, `random_state=42`
- **Valores de K probados:** 4, 5, 6, 7
- **Metrica de evaluacion:** Costo (suma total de disimilitudes entre cada punto y la moda de su cluster)

---

## 3. Resultados por Valor de K

### 3.1 K=4 (Modelo de Referencia)

**Costo: 150,855** | Total: 82,106 pacientes en 4 clusteres

| Cluster | Sexo | Topografia | Morfologia | Edad | Tamano |
|---------|------|------------|------------|------|--------|
| **0** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto Mayor | 24,851 (30.3%) |
| **1** | Hombre | Testiculo (C62.9) | Adenocarcinoma (8140) | Adulto | 22,583 (27.5%) |
| **2** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto | 21,752 (26.5%) |
| **3** | Mujer | Cuello uterino (C53.9) | NIC III (8077) | Adulto Joven | 12,920 (15.7%) |

**Interpretacion clinica:**
- **Cluster 0:** Mujeres mayores de 65 anos con cancer de mama. Perfil epidemiologico tipico: la incidencia de cancer de mama aumenta significativamente con la edad.
- **Cluster 1:** Hombres adultos (45-65 anos). Aunque la moda es testiculo, este cluster agrupa TODA la poblacion masculina adulta, mezclando patologias muy diferentes (testiculo, pulmon, colon, prostata, etc.). Es el cluster mas heterogeneo.
- **Cluster 2:** Mujeres adultas (45-65 anos) con cancer de mama. Se diferencia del cluster 0 unicamente por el rango de edad.
- **Cluster 3:** Mujeres adultas jovenes (18-45 anos) con lesiones precancerosas cervicales (NIC III). Este grupo es critico para programas de deteccion temprana del cancer cervical.

**Limitaciones de K=4:** Los clusters 0 y 2 solo se diferencian por edad. El cluster 1 mezcla TODA la patologia masculina sin distinguir entre cancer testicular (jovenes) y cancer de prostata (mayores).

---

### 3.2 K=5

**Costo: 141,494** (reduccion del 6.2% respecto a K=4)

| Cluster | Sexo | Topografia | Morfologia | Edad | Tamano |
|---------|------|------------|------------|------|--------|
| **0** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto Mayor | 17,172 (20.9%) |
| **1** | Hombre | Testiculo (C62.9) | Adenocarcinoma (8140) | Adulto | 22,396 (27.3%) |
| **2** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto | 21,752 (26.5%) |
| **3** | Mujer | Cuello uterino (C53.9) | NIC III (8077) | Adulto Joven | 12,920 (15.7%) |
| **4** | **Hombre** | **Prostata (C61.9)** | **Carcinoma escamoso (8070)** | **Adulto Mayor** | **7,866 (9.6%)** |

**Nuevo cluster (4) -- Cancer de prostata en adultos mayores:**
- 100% hombres, 97.6% mayores de 65 anos
- Topografia dominante: Prostata (15.3%), seguida de Rinon (5.1%) y Pulmon (4.9%)
- Este cluster separa a los hombres de edad avanzada del cluster 1, que ahora es mas puro en cancer de hombres adultos jovenes

**Interpretacion clinica del cambio K=4 a K=5:**
El avance mas importante es la **separacion de la patologia masculina por edad**: el cancer testicular predomina en hombres jovenes-adultos (cluster 1), mientras que el cancer de prostata predomina en adultos mayores (cluster 4). Esta distincion es clinicamente fundamental porque tienen perfiles de riesgo, tratamientos y pronosticos completamente diferentes.

**Distribucion de sexo por cluster:**
| Cluster | Hombre | Mujer |
|---------|--------|-------|
| 0 | 16.0% | 84.0% |
| 1 | 100.0% | 0.0% |
| 2 | 0.0% | 100.0% |
| 3 | 0.0% | 100.0% |
| 4 | 100.0% | 0.0% |

---

### 3.3 K=6

**Costo: 136,195** (reduccion del 3.7% respecto a K=5)

| Cluster | Sexo | Topografia | Morfologia | Edad | Tamano |
|---------|------|------------|------------|------|--------|
| **0** | Mujer | Mama (C50.9) | Adenocarcinoma (8140) | Adulto Mayor | 16,415 (20.0%) |
| **1** | Hombre | Testiculo (C62.9) | Adenocarcinoma (8140) | Adulto | 22,367 (27.2%) |
| **2** | Mujer | Cuello uterino (C53.9) | Adenocarcinoma (8140) | Adulto | 16,118 (19.6%) |
| **3** | Mujer | Cuello uterino (C53.9) | NIC III (8077) | Adulto Joven | 12,431 (15.1%) |
| **4** | Hombre | Prostata (C61.9) | Carcinoma escamoso (8070) | Adulto Mayor | 7,866 (9.6%) |
| **5** | **Mujer** | **Mama (C50.9)** | **Carcinoma ductal infiltrante (8500)** | **Adulto** | **6,909 (8.4%)** |

**Nuevos hallazgos en K=6:**

1. **Cluster 5 -- Cancer de mama con subtipo histologico especifico:**
   - 99.5% mujeres, 88.3% adultas (45-65 anos)
   - Topografia: Mama 84.2% concentrada, Cuadrante superior externo 7.3%
   - **Morfologia: Carcinoma Ductal Infiltrante (8500)** en lugar del Adenocarcinoma generico
   - Este es un hallazgo clinicamente relevante: el carcinoma ductal infiltrante es el subtipo mas comun y agresivo de cancer de mama. Identificarlo como grupo separado permite diferenciarlo de otros adenocarcinomas mamarios menos especificos.

2. **Cluster 2 migra a Cuello uterino adultas:**
   - 100% mujeres, 99.1% adultas (45-65 anos)
   - Topografias: Cuello uterino (14.6%), Cervix (6.6%), Endometrio (5.0%)
   - Se separa del cluster 3 (NIC III en jovenes): **cluster 2 captura canceres cervicales invasivos en mujeres adultas**, mientras que cluster 3 sigue siendo lesiones precancerosas en jovenes.

**Interpretacion clinica del cambio K=5 a K=6:**
Se logra una doble segmentacion importante:
- En **mama**: se separa el carcinoma ductal infiltrante (agresivo, invasivo) del adenocarcinoma generico
- En **cuello uterino**: se separa la patologia cervical por edad Y por gravedad (NIC III precanceroso en jovenes vs cancer invasivo en adultas)

---

### 3.4 K=7

**Costo: 131,579** (reduccion del 3.4% respecto a K=6)

| Cluster | Sexo | Topografia | Morfologia | Edad | Tamano |
|---------|------|------------|------------|------|--------|
| **0** | Mujer | Mama (C50.9) | Carcinoma, SAI (8010) | Adulto Mayor | 16,232 (19.8%) |
| **1** | Hombre | Testiculo (C62.9) | Carcinoma escamoso (8070) | Adulto | 19,068 (23.2%) |
| **2** | Mujer | Cuello uterino (C53.9) | Adenocarcinoma (8140) | Adulto | 14,857 (18.1%) |
| **3** | Mujer | Cuello uterino (C53.9) | NIC III (8077) | Adulto Joven | 11,912 (14.5%) |
| **4** | Hombre | Prostata (C61.9) | Adenocarcinoma (8140) | Adulto Mayor | 9,913 (12.1%) |
| **5** | Mujer | Mama (C50.9) | Carcinoma ductal infiltrante (8500) | Adulto | 5,826 (7.1%) |
| **6** | **Hombre** | **Recto (C20.9)** | **Adenocarcinoma (8140)** | **Adulto** | **4,298 (5.2%)** |

**Nuevo cluster (6) -- Cancer colorrectal masculino:**
- 100% hombres, 95.9% adultos (45-65 anos)
- Topografias: Recto 21.0%, Colon 11.1%, Pulmon 9.3%
- Morfologia: Adenocarcinoma (cancer glandular)
- Este cluster captura un perfil que estaba diluido en el cluster general de hombres: **cancer del tracto digestivo bajo en hombres adultos**

**Otros cambios notables en K=7:**
- **Cluster 4** (Prostata) crece a 9,913 pacientes (vs 7,866 en K=5/K=6), con 90.4% adultos mayores y 100% hombres. La separacion prostata vs testiculo es ahora mas neta.
- **Cluster 1** (Hombres Adultos) se reduce a 19,068 al perder el subgrupo colorrectal, pero sigue siendo el cluster masculino mas grande.
- **Cluster 0** (Mama Adulto Mayor) cambia su morfologia modal de Adenocarcinoma a **Carcinoma SAI** (8010), sugiriendo que al separarse subtipos especificos (ductal infiltrante en cluster 5), este cluster queda con la clasificacion mas generica.

**Distribucion de sexo por cluster (K=7):**
| Cluster | Hombre | Mujer |
|---------|--------|-------|
| 0 | 4.6% | 95.4% |
| 1 | 94.5% | 5.5% |
| 2 | 0.0% | 100.0% |
| 3 | 0.0% | 100.0% |
| 4 | 100.0% | 0.0% |
| 5 | 0.6% | 99.4% |
| 6 | 100.0% | 0.0% |

**Distribucion de edad por cluster (K=7):**
| Cluster | Infantil-Juvenil | Adulto Joven | Adulto | Adulto Mayor |
|---------|------------------|--------------|--------|--------------|
| 0 | 1.5% | 14.5% | 13.4% | 70.6% |
| 1 | 1.7% | 26.1% | 67.4% | 4.7% |
| 2 | 0.1% | 6.3% | 93.5% | 0.2% |
| 3 | 0.1% | 99.7% | 0.0% | 0.2% |
| 4 | 0.1% | 5.5% | 4.0% | 90.4% |
| 5 | 0.0% | 13.9% | 86.1% | 0.0% |
| 6 | 0.0% | 4.1% | 95.9% | 0.0% |

---

## 4. Analisis Comparativo

### 4.1 Evolucion del Costo

| K | Costo | Reduccion Absoluta | Reduccion Porcentual |
|---|-------|--------------------|----------------------|
| 4 | 150,855 | -- | -- |
| 5 | 141,494 | -9,361 | -6.2% |
| 6 | 136,195 | -5,299 | -3.7% |
| 7 | 131,579 | -4,616 | -3.4% |

La reduccion de costo se **desacelera** progresivamente, lo cual es esperado: cada cluster adicional aporta menor ganancia en cohesion. El mayor salto ocurre de K=4 a K=5.

### 4.2 Evolucion de los Tamanos de Cluster

| K | Tamano Min | Tamano Max | Promedio | Desviacion |
|---|------------|------------|----------|------------|
| 4 | 12,920 | 24,851 | 20,527 | 5,237 |
| 5 | 7,866 | 22,396 | 16,421 | 6,126 |
| 6 | 6,909 | 22,367 | 13,684 | 5,833 |
| 7 | 4,298 | 19,068 | 11,729 | 5,436 |

Observaciones:
- El cluster mas pequeno pasa de 12,920 (K=4) a 4,298 (K=7), pero sigue representando el **5.2% del total**, lo cual es estadisticamente robusto.
- La desviacion estandar de los tamanos se mantiene relativamente estable, indicando que no hay fragmentacion desproporcionada.

### 4.3 Mapa de Perfiles Descubiertos por K

| Perfil Clinico | K=4 | K=5 | K=6 | K=7 |
|---------------|-----|-----|-----|-----|
| Mama, Adulto Mayor | Si | Si | Si | Si |
| Mama, Adulto | Si | Si | -- | -- |
| Mama, Carcinoma Ductal Infiltrante, Adulto | -- | -- | Si | Si |
| Cuello uterino, NIC III, Adulto Joven | Si | Si | Si | Si |
| Cuello uterino, Adulto (invasivo) | -- | -- | Si | Si |
| Hombres, Testiculo, Adulto (general) | Si | Si | Si | Si |
| Hombres, Prostata, Adulto Mayor | -- | Si | Si | Si |
| Hombres, Colorrectal, Adulto | -- | -- | -- | Si |

**Patron de descubrimiento:** Cada incremento de K descubre un subgrupo que estaba "escondido" dentro de un cluster mas grande:
- K=5: Prostata se separa de Testiculo (distincion por edad en hombres)
- K=6: Ductal infiltrante se separa de Adenocarcinoma generico (distincion morfologica en mama) + Cuello uterino adulto se separa de NIC III joven
- K=7: Cancer colorrectal se separa del cluster masculino general (nueva topografia)

---

## 5. Discusion para Defensa

### 5.1 Por que usar K-Modes y no K-Means?

K-Means requiere que las variables sean numericas y calcula centroides como promedios. Nuestras variables principales (sexo, localizacion del tumor, tipo celular) son **categoricas**: no tiene sentido calcular el "promedio" entre "Mama" y "Testiculo". K-Modes resuelve esto:
- Usa la **moda** (valor mas frecuente) en lugar del promedio como centroide
- Mide disimilitud como el **numero de atributos diferentes** entre dos registros (distancia de Hamming)
- Es el algoritmo de clustering estandar para datos categoricos

### 5.2 Por que se eligio K=4 inicialmente?

Se aplico el **Metodo del Codo (Elbow Method)**: se entreno K-Modes para K=1 hasta K=10 y se grafico el costo total. El "codo" (punto donde la reduccion de costo se estabiliza) se identifico en K=4. Este es un criterio heuristico ampliamente aceptado.

### 5.3 Que aportan los experimentos con K=5, 6, 7?

Los experimentos demuestran que:

1. **K=4 es valido pero conservador.** Captura los patrones mas gruesos (mama, testiculo, cuello uterino) pero mezcla subpoblaciones clinicamente distintas.

2. **K=5 es la primera mejora significativa.** La separacion prostata/testiculo tiene alto impacto clinico:
   - Cancer testicular: hombres 15-45 anos, tratamiento con cirugia + quimioterapia, alta tasa de curacion
   - Cancer de prostata: hombres >65 anos, tratamiento con hormonoterapia + radioterapia, pronostico variable

3. **K=6 revela subtipos histologicos.** El Carcinoma Ductal Infiltrante (8500) es el subtipo mas comun de cancer de mama y tiene protocolos de tratamiento especificos. Identificarlo como grupo separado es util para:
   - Planificacion de recursos hospitalarios
   - Programas de deteccion (mamografia dirigida)
   - Estudios epidemiologicos de subtipos

4. **K=7 captura cancer colorrectal.** Este es uno de los canceres mas frecuentes a nivel mundial y su aparicion como cluster separado confirma su relevancia epidemiologica en la poblacion RITA.

### 5.4 Cual es el "mejor" K?

No existe un K "correcto" unico. La eleccion depende del **proposito**:

- **Para un resumen ejecutivo general:** K=4 es suficiente.
- **Para politicas de salud publica diferenciadas por sexo y edad:** K=5 es optimo.
- **Para analisis histopatologico y planificacion hospitalaria:** K=6 ofrece la mejor relacion entre detalle y parsimonia.
- **Para investigacion epidemiologica exhaustiva:** K=7 proporciona la mayor granularidad sin fragmentacion.

### 5.5 Limitaciones

1. **K-Modes es sensible a la inicializacion.** Usamos `n_init=5` para mitigar esto, pero corridas diferentes pueden producir asignaciones ligeramente distintas.
2. **La discretizacion de edad en 4 rangos pierde informacion.** Un enfoque alternativo seria usar K-Prototypes (que combina variables categoricas y numericas) para mantener la edad como variable continua.
3. **Las modas de los centroides muestran el valor MAS FRECUENTE, no el unico.** Un cluster con moda "Mama" puede contener pacientes con cancer de ovario, endometrio, etc. Las top-3 topografias por cluster (disponibles en el notebook) dan una vision mas completa.
4. **El metodo del codo es heuristico.** Otras metricas como el indice de silueta o el indice de Calinski-Harabasz podrian complementar la evaluacion.

---

## 6. Archivos Generados

| Archivo | Descripcion |
|---------|-------------|
| `rita_clusters_k4.csv` | Asignacion de cluster para cada paciente (K=4) |
| `rita_clusters_k5.csv` | Asignacion de cluster para cada paciente (K=5) |
| `rita_clusters_k6.csv` | Asignacion de cluster para cada paciente (K=6) |
| `rita_clusters_k7.csv` | Asignacion de cluster para cada paciente (K=7) |
| `resumen_k_experimentos.json` | Costos, tamanos y centroides en formato JSON |
| `figures/rita_cluster_geometry_k{K}.png` | Visualizacion PCA y t-SNE de los clusteres |
| `figures/rita_radar_profiles_k{K}.png` | Perfiles radar por cluster |
| `figures/rita_demographic_breakdown_k{K}.png` | Composicion demografica por cluster |

---

**Dataset:** RITA - Registro Institucional de Tumores de Argentina
**Algoritmo:** K-Modes (kmodes library, Python)
**Notebook de experimentacion:** `notebooks/06_experimentos_k5_k6_k7.ipynb`
