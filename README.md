# Simulador Estratégico de Productividad de Planta

Aplicación ejecutiva para cargar datos diarios de planta industrial, calcular productividad, analizar paradas y visualizar tendencias.

## Ejecutar en Streamlit

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Datos esperados

- Fecha
- OP
- Toneladas
- Horas operación
- Horas parada
- Causa principal
- Equipo / área afectada

El simulador también permite carga manual desde calendario, importación CSV/XLSX, KPIs, correlaciones, regresión múltiple y reportes ejecutivos.
