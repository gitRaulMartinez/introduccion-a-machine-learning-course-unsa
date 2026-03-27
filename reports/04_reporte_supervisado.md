# Reporte de Aprendizaje Supervisado: Clasificación de Pacientes

Este reporte presenta el desarrollo de modelos predictivos para clasificar el sexo del paciente basándose en el perfil diagnóstico de su enfermedad.

## 1. Selección de Atributos y Balanceo de Clases

### 1.1 Importancia de Características (Feature Importance)
- Se utilizó el modelo **Random Forest** para calcular la importancia intrínseca de cada variable.
- **Resultado:** Las variables `TOPOGRAFÍA_N` (Órgano afectado) y `MORFOLOGÍA_N` (Tipo de tumor) demostraron ser las de mayor peso predictivo, confirmando la estrecha relación biológica entre el órgano afectado y el sexo del paciente.

### 1.2 Tratamiento del Desbalanceo
- **Problema:** El dataset presentaba un desbalanceo de clases (~60% Mujeres, ~40% Hombres).
- **Acción:** Se aplicó la técnica **SMOTE** (Synthetic Minority Over-sampling Technique) al conjunto de entrenamiento, logrando una representación equitativa (50/50) para evitar el sesgo hacia la clase mayoritaria.

## 2. Desarrollo y Optimización de Modelos

Se desarrollaron dos modelos de clasificación de alta capacidad, optimizados mediante búsqueda en rejilla (**GridSearchCV**).

### Modelo 1: Random Forest (Clasificador de Bosques Aleatorios)
- **Precisión (Accuracy):** 0.77 (77%)
- **F1-Score:** 0.77
- **Análisis:** El modelo es robusto pero presenta algunas dificultades con diagnósticos compartidos por ambos sexos (ej: Estómago).

### Modelo 2: XGBoost (Extremo Impulso de Gradiente)
- **Precisión (Accuracy):** 0.784 (78.4%)
- **F1-Score:** 0.78
- **Análisis:** Superó ligeramente a Random Forest. Demostró una alta capacidad para capturar relaciones no lineales complejas entre la edad y la morfología del tumor.

## 3. Resultados y Métricas de Evaluación

Al comparar los dos modelos finales, el desempeño se resume en:

| Modelo | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | 0.771 | 0.790 | 0.771 | 0.770 |
| **XGBoost** | 0.784 | 0.840 | 0.784 | 0.780 |

### Matriz de Confusión (Hallazgos)
Los modelos son extremadamente precisos al identificar tumores específicos de órganos (Mama, Próstata, Cuello Uterino), pero presentan errores en diagnósticos generales como "Adenocarcinoma de Sitio Primario No Especificado", donde la variabilidad biológica es mayor.

## 4. Conclusión Estratégica
XGBoost se recomienda como el modelo de producción final debido a su mayor precisión global. El proyecto demuestra que la información diagnóstica disponible tiene un alto valor predictivo demográfico.
