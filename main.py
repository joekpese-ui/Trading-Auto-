import pandas as pd
import numpy as np
import yfinance as yf

# Définir les marchés à trader
markets = ['EURUSD', 'USDJPY', 'GBPUSD']

# Définir les indicateurs techniques à utiliser
indicators = ['RSI', 'MACD']

# Définir la fonction de trading
def trade(market, indicator):
    # Récupérer les données financières
    data = yf.download(market, period='1d')

    # Calculer les indicateurs techniques
    if indicator == 'RSI':
        rsi = pd.Series(data['Close'].rolling(window=14).mean())
        print(f'RSI pour {market} : {rsi.iloc[-1]}')
    elif indicator == 'MACD':
        macd = pd.Series(data['Close'].ewm(span=12, adjust=False).mean() - data['Close'].ewm(span=26, adjust=False).mean())
        print(f'MACD pour {market} : {macd.iloc[-1]}')

# Lancer la fonction de trading
for market in markets:
    for indicator in indicators:
        trade(market, indicator)
