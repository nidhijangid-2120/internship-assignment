# Study the open weather API show more data in your API calling program
import requests
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e02619def95ad1b6d49357c9f244ee79&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors
        data = response.json()
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    except requests.RequestException as e:
        print(f'Error fetching data for {city}: {e}')
city = input("Enter a city name: ")
get_weather_data(city)