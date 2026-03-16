**Objetivo de la Tarea:**
Desarrollar un modelo de Aprendizaje No Supervisado utilizando el algoritmo K-Modes, dado que el dataset (registros oncológicos) ha sido tratado con un enfoque mayoritariamente categórico. El objetivo es descubrir agrupamientos (clústeres) ocultos en los perfiles de los pacientes, sin utilizar etiquetas previas.

---

**Parte 1: Selección de Atributos y Preparación**
*   **Atributos de entrada y justificación:** Seleccionar las columnas categóricas relevantes para el agrupamiento (por ejemplo: `PTESXN` - Sexo, `TOPOGRAFÍA` y `MORFOLOGÍA` recodificadas/simplificadas, y `EDAD_DIAGNÓSTICO` discretizada). Se debe escribir una breve justificación clínica y técnica de por qué se eligieron estas variables y por qué se descartaron otras (como el ID del paciente) [1].
*   **Recodificación para K-Modes:** Dado que la librería `kmodes` requiere que las categorías estén representadas numéricamente, aplicar `LabelEncoder` o diccionarios para transformar los datos categóricos a números enteros antes de ingresarlos al modelo [3, 4].

**Parte 2: Determinación del número de grupos (K)**
*   **Método de Elbow (Codo):** Implementar un bucle iterativo (por ejemplo, de K=1 a K=10) utilizando el modelo `KModes(init="random")`. 
*   **Costo:** En cada iteración, guardar el atributo de costo (`modelKmode.cost_`) en lugar de la inercia (WCSS) que se usa en K-Means [5].
*   **Visualización:** Graficar el número de clústeres versus el Costo para identificar visualmente el "codo" y decidir el número óptimo de grupos (K) [6].

**Parte 3: Desarrollo del Modelo y Predicción**
*   **Entrenamiento:** Instanciar el modelo K-Modes definitivo con el número K óptimo encontrado en el paso anterior.
*   **Predicción:** Entrenar el modelo y predecir los clústeres (`fit_predict()`), asignando el resultado como una nueva columna en el DataFrame original para facilitar su análisis [7, 8].

**Parte 4: Interpretación de los Grupos y Métricas**
*   **Análisis de los Centroides (Modas):** Imprimir los centroides del modelo. Al ser K-Modes, estos centroides representan la "moda" (características más frecuentes) de cada grupo [9, 10].
*   **Interpretación:** Analizar estadísticamente cada clúster (por ejemplo, filtrando el DataFrame por grupo o usando `groupby()`) y redactar una interpretación detallada indicando qué representa cada grupo en el contexto clínico (ej. "El Clúster 0 representa principalmente a mujeres adultas mayores con cáncer de mama...") [2, 11, 12].
*   **Métricas:** Mostrar la distribución (frecuencia o tamaño) de los datos en cada clúster y registrar el costo final obtenido por el modelo como métrica principal de la cohesión del grupo [2, 5].