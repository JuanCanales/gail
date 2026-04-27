
from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import numpy as np
import pandas_ta as ta # Asegúrate de importar esta librería

app = Flask(__name__)


def obtener_analisis(ticker):
    data = yf.download(ticker, period="2y", interval="1d")
    
    if data.empty: return None
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # 1. Cálculo de Indicadores
    # Media Móvil de 50 días (largo plazo)
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # Media Móvil de 7 días (semanal)
    data['SMA_7'] = data['Close'].rolling(window=7).mean()
    
    # RSI de 14 periodos
    data['RSI'] = ta.rsi(data['Close'], length=14)
    
    # 2. Extracción de valores actuales
    precio_actual = float(data['Close'].iloc[-1])
    sma_50 = float(data['SMA_50'].iloc[-1])
    sma_7 = float(data['SMA_7'].iloc[-1])
    rsi_actual = float(data['RSI'].iloc[-1])
    
    # 3. Soporte/Resistencia semanal
    data_semana = data.tail(5)
    soporte_semana = float(data_semana['Close'].min())
    resistencia_semana = float(data_semana['Close'].max())
    
    return {
        "precio_actual": round(precio_actual, 2),
        "sma_7": round(sma_7, 2),
        "rsi": round(rsi_actual, 2),
        "soporte_semana": round(soporte_semana, 2),
        "resistencia_semana": round(resistencia_semana, 2),
        "tendencia_largo": "Alcista" if precio_actual > sma_50 else "Bajista",
        "estado_rsi": "Sobrecompra (>70)" if rsi_actual > 70 else ("Sobreventa (<30)" if rsi_actual < 30 else "Neutral")
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        resultado = obtener_analisis(ticker)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
