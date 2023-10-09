import requests
import json

url = " http://api.weatherapi.com/v1/current.json?key=e4e954117008449da6581103231306&q="+input("Enter your city name:-")

df = requests.get(url)
data = json.loads(df.content)
print(f"Temperature of {data['location']['name']} is {data['current']['temp_c']}")



