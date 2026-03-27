# Resultados Integrados - Students (Columnas en Espanol)

## 1) Resumen ejecutivo

Se completo el flujo limpieza -> EDA -> no supervisado -> supervisado usando nomenclatura de columnas en espanol para mejorar comprension en notebooks y reportes.

## 2) Hallazgos por fase

### Limpieza
- 31 columnas normalizadas y traducidas al espanol tecnico.
- Dataset limpio final: 1194 registros.
- Nulos residuales: 2.
- Outliers en `edad` por IQR: 13.

### EDA
- `sexo`: Male 672, Female 522.
- `alguna_vez_probation`: No 896, Yes 298 (desbalance moderado).
- `edad` media: 21.34.
- `cgpa_actual` medio: 3.17.

### No supervisado (K-Modes)
- Variables categoricas de perfil y contexto.
- K evaluado 1..8, seleccionado K=4.
- Segmentos obtenidos: 4 perfiles interpretables para acciones diferenciadas.

### Supervisado (target `alguna_vez_probation`)
- Modelos: Random Forest y XGBoost con SMOTE.
- Mejor modelo por F1 positivo: **XGBoost**.
- Metricas XGBoost: Accuracy 0.8326, Precision 0.7273, Recall 0.5333, F1 0.6154.

## 3) Justificacion tecnica de decisiones

- **K-Modes:** por predominio de variables categoricas.
- **K=4:** balance entre costo, interpretabilidad y aplicabilidad academica.
- **Target probation:** mejor etiqueta disponible para riesgo academico temprano.
- **SMOTE:** necesario para reducir sesgo por desbalance de clase.

## 4) Recomendacion final

Usar XGBoost como base de alerta academica y complementar con clusters K-Modes para personalizar estrategias de acompanamiento segun perfil estudiantil.
