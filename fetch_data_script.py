import pandas as pd
import ccxt
from datetime import datetime, timedelta

# Configurar el exchange
exchange = ccxt.binance()

# Definir el par de trading y el intervalo de tiempo
symbol = 'ETH/USDT'
timeframe = '5m'

# Calcular las fechas de inicio y fin
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Convertir las fechas a timestamps en milisegundos
since = int(start_date.timestamp() * 1000)
until = int(end_date.timestamp() * 1000)

# Obtener los datos en lotes de 1000 registros
batch_size = 1000
bars = []
current_since = since

while current_since < until:
    current_until = min(current_since + batch_size * 300000, until)  # Incrementar el since en 300000 ms por batch
    ohlcv_batch = exchange.fetch_ohlcv(symbol, timeframe, current_since, current_until)
    bars += ohlcv_batch
    current_since = ohlcv_batch[-1][0] + 300000  # Actualizar el since al final del batch

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Establecer la columna de tiempo como índice
df.set_index('timestamp', inplace=True)

# Guardar los datos en un archivo Parquet
df.to_csv('ETH-1-Year-5min.csv')

