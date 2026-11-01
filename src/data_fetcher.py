import yfinance as yf

def price_series(ticker_symbol):
    
    ticker = yf.Ticker(f"{ticker_symbol}.SA")

    historical_data = ticker.history(period="5d")

    if historical_data.empty:
        raise ValueError(f"Sem dados para {ticker_symbol}!")
    
    close_prices = historical_data["Close"] 
    
    return close_prices