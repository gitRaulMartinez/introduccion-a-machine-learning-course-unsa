# Informe Final de Proyecto: Análisis de Datos Oncológicos (RITA)

Este documento unifica el proceso de pre-procesamiento, análisis exploratorio y modelado de Machine Learning aplicado al conjunto de datos oncológicos "RITA".

---

## 1. Fase 1: Pre-procesado y Limpieza de Datos

El objetivo inicial fue asegurar la calidad de los datos para evitar sesgos en los modelos posteriores.

### Acciones Realizadas:
1. **Limpieza de Nombres:** Se normalizaron las columnas eliminando espacios en blanco.
2. **Tratamiento de Nulos:** Se identificaron y trataron valores faltantes en `TOPOGRAFÍA` y `MORFOLOGÍA`.
3. **Outliers:** Se utilizó el método del Rango Intercuartílico (IQR) para detectar edades de diagnóstico atípicas.
4. **Recodificación:** Se transformó la variable Sexo (`PTESXN`) a numérica (`SEXO_NUM`) para el procesamiento algorítmico.

---

## 2. Fase 2: Análisis Exploratorio de Datos (EDA)

Se realizó un análisis estadístico y visual para comprender la distribución de las variables.

### Hallazgos Principales:
- La edad promedio de diagnóstico es de **55 años**.
- Las mujeres representan el **60%** de los casos registrados.
- Existe una clara diferencia en la edad de diagnóstico según el sexo.

### Visualizaciones:
![Distribución de Edad](figures/01_histograma_edad.png)
*Figura 1: Distribución de la edad de diagnóstico en la población analizada.*

![Matriz de Correlación](figures/02_matriz_correlacion.png)
*Figura 2: Relaciones lineales entre las variables numéricas del dataset.*

---

## 3. Fase 3: Aprendizaje No Supervisado (Clustering)

Utilizamos el algoritmo **K-Modes** para descubrir perfiles ocultos de pacientes basándonos en variables categóricas.

### Resultados:
- Se determinó que **K=4** es el número óptimo de grupos mediante el método del codo.
- Los clústeres identificaron perfiles específicos, como "Mujer adulta mayor con cáncer de mama" y "Mujer joven con cáncer de cuello uterino".

### Selección del Número de Grupos:
![Curva de Elbow](figures/03_curva_elbow.png)
*Figura 3: Determinación del número óptimo de clústeres (K=4).*

---

## 4. Fase 4: Aprendizaje Supervisado (Clasificación)

Desarrollamos modelos para predecir el sexo del paciente a partir de su perfil diagnóstico.

### Modelos y Desempeño:
- **XGBoost** resultó ser el modelo más preciso con un **78.4% de Accuracy**.
- Se aplicó **SMOTE** para balancear las clases (Hombre/Mujer) y mejorar la detección de la clase minoritaria.

### Evaluación del Modelo:
![Matriz de Confusión](figures/04_matriz_confusion.png)
*Figura 4: Matriz de confusión para el modelo de Random Forest.*

---

## 5. Conclusiones Finales

1. Los modelos diagnósticos demuestran una alta capacidad para identificar perfiles demográficos.
2. La topografía y morfología del tumor son los mejores predictores clínicos.
3. El pre-procesamiento riguroso fue clave para obtener métricas de desempeño confiables superiores al 77%.
