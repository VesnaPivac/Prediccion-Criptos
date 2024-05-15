# Predicción del Precio de Ethereum (ETH) con Red LSTM

Este repositorio contiene el código y los archivos necesarios para entrenar y utilizar una red neuronal LSTM para predecir el precio de la criptomoneda Ethereum (ETH) utilizando datos históricos.

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar un modelo de aprendizaje profundo que pueda predecir el precio de la criptomoneda Ethereum basado en su historial de precios y otros factores relevantes. Se emplea una red neuronal LSTM debido a su capacidad para capturar patrones secuenciales en datos temporales, lo que es fundamental para el análisis de series temporales como el precio de las criptomonedas.

## Estructura del Repositorio

- `modelo_final.h5`: Modelo que se entreno y utilizo para predecir.
- `fetch_data_script.py`: Archivo de python en el que se realiza la descarga de los datos de la criptomoneda
- `PredecirCriptoFinal.ipynb`: Jupyter Notebooks donde se realizo la lectura de los datos, el entrenamiento y la prediccion.
- `ETH-1-Year-5min.csv`: Archivo csv en el que se encuentran los datos descargados.

## Instalación, Requisitos y Usp

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener instalado Python 3 y las siguientes bibliotecas:
   - Pandas
   - NumPy
   - Matplotlib
   - Jupyter Notebook
   - ccxt
3. Descarga los datos históricos de Ethereum ejecutando en la consola de comandos la siguiente instruccion:
   ```
   python fetch_data_script.py
   ```
   Esto te generara el archivo parquet donde estaran los datos que se utilizaran desde la fecha actual hasta un año atras con registros de cada 5 minutos.
4. Ejecutar la libreta PredecirCriptoFinal.ipynb




## Créditos
- [PythonIA](https://www.youtube.com/watch?v=qnPeHaO2Q3k)
