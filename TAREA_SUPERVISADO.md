**Objetivo General de la Tarea:**
Desarrollar, optimizar y evaluar modelos predictivos de Aprendizaje Supervisado para clasificar la variable objetivo del dataset. Se deben construir 2 modelos en total elegidos entre las técnicas permitidas, aplicando un tratamiento riguroso de selección de variables y balanceo de clases [3].

---

**Parte 1: Selección de Atributos**
*   **Reducción de dimensionalidad / Filtrado:** Aplicar y justificar matemáticamente la técnica utilizada para seleccionar las características más relevantes antes de entrenar los modelos [1]. Se debe utilizar obligatoriamente al menos una de las siguientes técnicas:
    *   *Feature Importance* (usando modelos intrínsecos).
    *   *RFE* (Eliminación Recursiva de Características, técnica envolvente).
    *   *ACP* (Análisis de Componentes Principales, técnica de extracción).

**Parte 2: Tratamiento del Desbalanceo**
*   **Balanceo de Clases:** Analizar la distribución de las etiquetas en la variable de salida (objetivo). Implementar técnicas para mitigar el desbalanceo de los datos (por ejemplo, mediante técnicas de sobremuestreo como SMOTE, submuestreo, o balanceo de pesos en los algoritmos) para asegurar que el modelo no se sesgue hacia la clase mayoritaria [1].

**Parte 3: Entrenamiento y Optimización de Modelos**
*   **Selección de Algoritmos:** Instanciar y desarrollar **2 modelos** predictivos eligiendo entre las siguientes técnicas permitidas: Random Forest (RF), Support Vector Machines (SVM), XGBoost o Extreme Learning Machines (ELM) [3].
*   **Validación y Configuración:** Aplicar técnicas de validación cruzada (*cross-validation*) para evaluar la robustez del modelo y realizar la búsqueda de los mejores *hiper-parámetros* (por ejemplo, usando GridSearchCV o RandomizedSearchCV) [1].

**Parte 4: Resultados y Métricas de Evaluación**
*   **Evaluación Global (Nivel Modelo):** Calcular y presentar el rendimiento general de cada uno de los dos modelos desarrollados (ej. Accuracy general) [2].
*   **Evaluación por Clase (Nivel Predicción):** Generar e interpretar la Matriz de Confusión y extraer las métricas detalladas para cada una de las clases predichas (Precision, Recall, F1-Score) [2].
*   **Conclusión:** Analizar los resultados comparando ambos modelos y argumentar cuál tuvo el mejor desempeño resolviendo el problema planteado.