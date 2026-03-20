# Reporte de Aprendizaje No Supervisado: Agrupamiento con K-Modes

Este reporte detalla el desarrollo de un modelo de segmentación de pacientes oncológicos utilizando el algoritmo K-Modes, adecuado para conjuntos de datos con alta predominancia de variables categóricas.

## 1. Selección y Preparación de Atributos

### 1.1 Variables Seleccionadas
- **PTESXN (Sexo):** Diferenciación biológica fundamental.
- **TOPOGRAFÍA_N:** Localización anatómica del tumor.
- **MORFOLOGÍA_N:** Tipo histológico de las células cancerígenas.
- **EDAD_RANGO:** Variable discretizada en 4 categorías: Infantil-Juvenil (0-18), Adulto Joven (18-45), Adulto (45-65) y Adulto Mayor (65+).

### 1.2 Justificación Técnica
Se utilizó **K-Modes** en lugar de K-Means debido a que la mayor parte de la información diagnóstica es categórica (texto). El uso de `LabelEncoder` permitió codificar las categorías para el cálculo de disimilitudes sin imponer un orden numérico falso.

## 2. Determinación del Número de Grupos (K)

### 2.1 Método del Codo (Elbow Method)
- Se realizaron iteraciones del modelo para K de 1 a 10.
- Se evaluó el **Costo (Suma de disimilitudes)** en lugar de la inercia convencional.
- **Resultado:** Se identificó que el punto de inflexión óptimo ocurre en **K = 4**, donde la reducción del costo se estabiliza.

## 3. Interpretación de los Clústeres (Modas)

El modelo logró segmentar a los pacientes en 4 perfiles predominantes (Centroides):

| Clúster | Sexo | Topografía (Órgano) | Morfología (Tipo de Célula) | Edad (Rango) | Tamaño (N) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | Mujer | Mama (C50.9) | Adenocarcinoma | Adulto Mayor | 24,851 |
| **1** | Hombre | Testículo (C62.9) | Adenocarcinoma | Adulto | 22,583 |
| **2** | Mujer | Mama (C50.9) | Adenocarcinoma | Adulto | 21,752 |
| **3** | Mujer | Cuello Uterino (C53.9) | Neoplasia Intraepitelial | Adulto Joven | 12,920 |

## 4. Conclusiones del Modelo
- **Segmentación Clínica:** El modelo identifica correctamente los tumores de mayor incidencia (Mama y Cuello Uterino) y los asocia con perfiles de edad específicos.
- **Homogeneidad:** El clúster 0 es el más grande y homogéneo, representando el perfil típico de cáncer de mama en edad avanzada.
- **Utilidad:** Esta segmentación permite priorizar políticas de salud pública diferenciadas por grupos de riesgo detectados automáticamente.
