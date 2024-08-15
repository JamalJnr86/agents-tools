#search_tool.py
import requests #type: ignore


API_KEY = "AIzaSyDzv2mW64JiZz-siaK5mQumvvMv0N3FGiA"
CX = "267b6e63b35f44cff"

def search_web(query, num_results=5):
    
    api_key = "AIzaSyDzv2mW64JiZz-siaK5mQumvvMv0N3FGiA"
    cx = "267b6e63b35f44cff"

    # Define the endpoint and parameters
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": num_results,
    }

    try:
        # Make the request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        results = response.json()

        # Extract titles and links from the search results
        search_items = results.get("items", [])
        search_results = []
        for item in search_items:
            title = item.get("title")
            link = item.get("link")
            search_results.append({"title": title, "link": link})

        return search_results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

