import requests  # type: ignore

def convert_currency(amount, from_currency, to_currency):
    api_key = "c479d82a10b888f28eec7ec1"  # Ensure this is a valid API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        data = response.json()
        rate = data.get("conversion_rate")
        
        if rate is not None:
            converted_amount = amount * rate
            return f"{amount} {from_currency} is equal to {converted_amount:.3f} {to_currency}."
        else:
            return "Conversion rate not found in the response."
    
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"
    except ValueError as e:
        return f"Error parsing response: {str(e)}"
    except KeyError as e:
        return f"Unexpected response format: {str(e)}"
