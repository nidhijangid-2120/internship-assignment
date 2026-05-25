# Search for more free API's generate your and call them to fetch data. Display some data in your program.
import requests
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors
        joke = response.json()
        print(f"Here's a random joke for you:\n{joke['setup']}\n{joke['punchline']}")
    except requests.RequestException as e:
        print(f'Error fetching joke: {e}')
get_random_joke()

