# Experimentos K-Modes en RITA (K=4..8)

Se probaron K=4,5,6,7,8 para analizar variación de costos, tamaños de cluster, geometría y composición demográfica.

## Configuracion
- Dataset: `data/processed/rita/rita_limpio.csv`
- Filas usadas: 82106
- Variables: `PTESXN`, `TOPOGRAFÍA_N`, `MORFOLOGÍA_N`, `EDAD_RANGO`
- Geometría (PCA/t-SNE): muestra estratificada de 12000 puntos para visualización

## Resumen de resultados por K
- **K=4** | Costo: **147993.0** | Tamaños: C0:23806, C1:19656, C2:22167, C3:16477
- **K=5** | Costo: **142062.0** | Tamaños: C0:29311, C1:17999, C2:10960, C3:10916, C4:12920
- **K=6** | Costo: **142928.0** | Tamaños: C0:33156, C1:16119, C2:12927, C3:10620, C4:7380, C5:1904
- **K=7** | Costo: **135263.0** | Tamaños: C0:16605, C1:17494, C2:21194, C3:10384, C4:2655, C5:11970, C6:1804
- **K=8** | Costo: **132441.0** | Tamaños: C0:16445, C1:18212, C2:15779, C3:7976, C4:9426, C5:4810, C6:2363, C7:7095

## Archivos generados
- CSV por K: `reports/rita/k_experimentos/rita_clusters_k{K}.csv`
- Geometría: `reports/rita/k_experimentos/figures/rita_cluster_geometry_k{K}.png`
- Radar: `reports/rita/k_experimentos/figures/rita_radar_profiles_k{K}.png`
- Composición: `reports/rita/k_experimentos/figures/rita_demographic_breakdown_k{K}.png`