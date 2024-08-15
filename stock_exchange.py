#stock_exchaneg.py
import requests  # type: ignore

def get_stock_exchange_rate(index_symbol):
    stock_api_key = "Add_your_api_exchangerate_api"  # Replace with your actual API key
    result = {}

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={index_symbol}&interval=1min&apikey={stock_api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        time_series = data.get("Time Series (1min)")
        
        if time_series:
            latest_time = max(time_series.keys())
            latest_data = time_series[latest_time]
            closing_price = latest_data.get("4. close")
            result[index_symbol] = closing_price
        else:
            result[index_symbol] = "Data not found."
    
    except requests.exceptions.RequestException as e:
        result[index_symbol] = f"Request error: {str(e)}"
    except ValueError as e:
        result[index_symbol] = f"Error parsing response: {str(e)}"
    except KeyError as e:
        result[index_symbol] = f"Unexpected response format: {str(e)}"
    
    return result
