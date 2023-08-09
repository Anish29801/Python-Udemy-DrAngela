import requests

location = input('Enter your city : ')
url = "https://api.openweathermap.org/data/2.5/weather?q=+"+location+"&units=imperial&appid=895284fb2d2c50a520ea537456963d9c"
print('Loading weather data..')
try:
    response = requests.get(url)
    response = response.json()
    print(response["main"])
    print(response["main"]['temp'])
except Exception as e:
    print ("Failed to load weather data")