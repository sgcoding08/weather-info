import requests  

API_KEY = "your_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    print(f"Weather in {city}: {weather}, {temp}°C, {humidity}% humidity")
else:
    print("City not found.")

