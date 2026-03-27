# Reporte de Resultados: Análisis de Datos Oncológicos (RITA)

Este documento resume los hallazgos obtenidos tras la ejecución de los modelos de Aprendizaje No Supervisado (K-Modes) y Supervisado (Random Forest y XGBoost).

---

## 1. Análisis No Supervisado (Segmentación con K-Modes)

El algoritmo K-Modes identificó **4 grupos principales (clústeres)** de pacientes basados en patrones de diagnóstico, sexo y edad.

### Perfil de los Clústeres:
*   **Clúster 0 (24,851 pacientes):** Mujeres adultas mayores con diagnósticos de **Cáncer de Mama (C50.9)** y morfología de **Adenocarcinoma**. Es el grupo más numeroso, reflejando la alta incidencia de este tipo de cáncer en la población femenina de edad avanzada.
*   **Clúster 1 (22,583 pacientes):** Hombres adultos. Un hallazgo interesante es la moda de **Cáncer de Testículo (C62.9)**, indicando un segmento significativo de la población masculina joven/adulta.
*   **Clúster 2 (21,752 pacientes):** Mujeres adultas con **Cáncer de Mama**. A diferencia del clúster 0, este agrupa a mujeres en un rango de edad más joven (Adultas), lo que permite diferenciar perfiles epidemiológicos por edad.
*   **Clúster 3 (12,920 pacientes):** Mujeres adultas jóvenes con **Cáncer de Cuello Uterino (C53.9)** y neoplasias intraepiteliales. Este grupo es crítico para políticas de prevención temprana.

**Conclusión:** El modelo logró separar con éxito las patologías género-específicas (mama, testículo, cuello uterino) y segmentarlas por etapas de vida.

---

## 2. Análisis Supervisado (Clasificación de Sexo)

El objetivo fue predecir el sexo del paciente basándose únicamente en variables clínicas.

### Comparativa de Modelos:
| Métrica | Random Forest (RF) | XGBoost |
| :--- | :---: | :---: |
| **Accuracy (Exactitud)** | 77.07% | **78.44%** |
| **F1-Score (Hombres - Clase 0)** | 0.74 | **0.78** |
| **F1-Score (Mujeres - Clase 1)** | 0.79 | 0.79 |
| **Recall (Hombres)** | 0.82 | **0.96** |

### Hallazgos Clave:
1.  **Mejor Modelo:** **XGBoost** superó ligeramente a Random Forest. Destaca especialmente su **Recall en hombres (0.96)**, lo que significa que casi no omite casos masculinos (pocos falsos negativos para la clase 0).
2.  **Importancia de Variables:** La **Topografía (Localización del tumor)** fue la variable más importante. Esto es lógico: si el tumor está en la próstata o útero, el sexo queda definido automáticamente. La **Edad** también aportó valor discriminante.
3.  **Efecto del Balanceo (SMOTE):** Gracias al sobremuestreo de la clase minoritaria (Hombres), ambos modelos lograron un rendimiento equilibrado. Sin SMOTE, el modelo tendería a predecir siempre "Mujer" debido a la mayor frecuencia en el dataset.

---

## 3. Explicación Técnica de los Procedimientos

*   **¿Por qué K-Modes?:** Usamos K-Modes en lugar de K-Means porque la mayoría de nuestros datos (Topografía, Morfología, Sexo) son **categóricos**. K-Means mide distancias euclidianas (inútiles en texto), mientras que K-Modes mide **disimilitud basada en coincidencias**.
*   **¿Por qué SMOTE?:** El dataset tenía más mujeres que hombres. Si entrenamos así, el modelo se vuelve "perezoso" y predice la mayoría para acertar más. SMOTE crea datos sintéticos de hombres para que el modelo aprenda sus patrones con la misma importancia.
*   **¿Por qué Random Forest y XGBoost?:** Son modelos de "Ensamble" basados en árboles de decisión. Son excelentes para manejar relaciones no lineales y datos categóricos codificados sin requerir una normalización estricta.

---
**Elaborado por:** Gemini CLI
**Fecha:** 16 de marzo de 2026
