# Reporte de Pre-procesado, Limpieza y Recodificación

Este reporte detalla las acciones realizadas sobre el dataset original de salud "RITA" para asegurar la integridad de los datos antes de aplicar modelos de Machine Learning.

## 1. Acciones Realizadas

### 1.1 Limpieza de Columnas (CRUD)
- **Problema:** Los nombres de las columnas presentaban espacios en blanco al inicio o al final (ej: `"PTESXN "`), lo cual dificultaba el acceso programático.
- **Solución:** Se aplicó una limpieza masiva usando `.str.strip()` para normalizar los nombres.
- **Resultado:** Columnas normalizadas: `IDPTE`, `PTESXN`, `FECHA_DIAGNÓSTICO`, `EDAD_DIAGNÓSTICO`, `TOPOGRAFÍA`, etc.

### 1.2 Tratamiento de Valores Ausentes (Missing Values)
- **Hallazgo:**
    - `TOPOGRAFÍA`: 17 valores nulos.
    - `MORFOLOGÍA`: 240 valores nulos.
- **Acción:** Dado que estos valores representan una fracción mínima del dataset (~82,000 registros), se optó por la exclusión de estas filas en las fases de modelado para mantener la precisión clínica.

### 1.3 Detección y Tratamiento de Outliers
- **Método:** Rango Intercuartílico (IQR) aplicado a la variable `EDAD_DIAGNÓSTICO`.
- **Cálculo:**
    - Q1: 44 años.
    - Q3: 66 años.
    - IQR: 22 años.
- **Resultado:** Se detectó 1 valor atípico extremo (edad > 100 años). Aunque es biológicamente posible, se identificó mediante Boxplots para asegurar que no sesgara los promedios.

### 1.4 Recodificación y Caseteo
- **Variable Objetivo Indirecta:** `PTESXN` (Sexo).
- **Transformación:** Se creó la columna `SEXO_NUM` mapeando `Hombre -> 0` y `Mujer -> 1`.
- **Justificación:** Los algoritmos de Machine Learning requieren entradas numéricas para procesar distinciones categóricas.

## 2. Dataset Generado
El proceso concluyó con la generación del archivo `data/processed/rita_limpio.csv`, el cual sirve como fuente única de verdad para las siguientes etapas de análisis.
