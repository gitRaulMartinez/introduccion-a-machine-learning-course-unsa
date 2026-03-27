# Resumen del Proyecto (RITA)

Este proyecto sigue una ruta completa de analisis de datos y machine learning en 4 etapas principales:

1. **Limpieza y preprocesado de datos**
   - Normalizacion de nombres de columnas.
   - Revision y tratamiento de valores nulos en variables clave.
   - Deteccion de outliers en edad (IQR).
   - Recodificacion de variables categoricas para modelado.

2. **EDA (Analisis Exploratorio de Datos)**
   - Estadistica descriptiva general (`describe`, `info`, distribuciones).
   - Comparaciones por grupos (por ejemplo, edad por sexo).
   - Visualizaciones univariadas y multivariadas.
   - Hallazgos para guiar decisiones de modelado.

3. **Aprendizaje no supervisado**
   - Seleccion de variables categoricas relevantes.
   - Codificacion para aplicar **K-Modes**.
   - Busqueda de `K` optimo con metodo del codo (costo).
   - Entrenamiento, asignacion de clusters e interpretacion de perfiles.

4. **Aprendizaje supervisado**
   - Definicion de variable objetivo (clasificacion).
   - Seleccion de atributos (Feature Importance / RFE / PCA segun necesidad).
   - Tratamiento de desbalanceo (SMOTE u otra tecnica).
   - Entrenamiento y comparacion de al menos 2 modelos (RF, SVM, XGBoost, etc.).
   - Evaluacion con Accuracy, Precision, Recall, F1 y Matriz de Confusion.

## Resultado general

El flujo aplicado permite pasar de un dataset crudo a modelos interpretables y evaluados, con una estructura reutilizable para nuevos datasets.
