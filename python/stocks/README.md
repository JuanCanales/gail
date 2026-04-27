Aplicacion que coge los ultimos 2 años de cierre de precios de un stock y calcula soportes y resistencias historicos y de la ultima semana

Prompt : creame una web en python flask que se descargue los ultimos años de cierre de precios del dia de un stock price que le indique en un campo, y me calcule donde estan los soportes, resistencias, tendencias , y prediga si el precio va a subir o bajar
Output : Consideraciones importantes:

1. Predicciones: He incluido un modelo de LinearRegression de scikit-learn. Advertencia: El mercado de valores es estocástico (caótico). Una regresión lineal simple no puede predecir el futuro con exactitud y solo sirve para fines educativos. No uses esto para invertir dinero real.

2. Análisis Técnico: Los soportes y resistencias aquí son calculados como el mínimo y máximo de 2 años. En trading profesional, se usan niveles Fibonacci, puntos pivote o volúmenes de negociación.

Por qué esto es útil?

• Soporte/Resistencia Semanal: Te indican el rango de corto plazo (volatilidad reciente). Si el precio rompe el soporte semanal, es una señal de debilidad inmediata aunque el precio esté muy por encima del soporte histórico de 2 años.

• Soporte/Resistencia Histórica: Te indican los niveles de largo plazo. Son niveles psicológicos mucho más fuertes donde es más probable que el precio rebote o sufra una resistencia mayor.

Nota técnica: Si el mercado ha estado cerrado (ej. fin de semana), tail(5) te traerá los últimos 5 días en los que efectivamente hubo operaciones.

Prompt 2 : añademe el RSI y moving average de la ultima semana


Cómo ejecutar:

1. Ejecuta python app.py.

2. Abre tu navegador en http://127.0.0.1:5000.
